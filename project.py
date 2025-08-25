from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder 
from langchain_ollama import ChatOllama , OllamaEmbeddings
from langchain.schema import Document
from langchain.vectorstores import FAISS  # using Chroma instead of FAISS mentioned in the documents 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnableSequence , RunnableParallel , RunnableLambda , RunnableBranch , RunnablePassthrough
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_core.output_parsers import StrOutputParser

# setting up the models :

model = ChatOllama(model="llama3.1")
embedding_model = OllamaEmbeddings(model="nomic-embed-text")

# GETTING THE DOCUMENT (document Loader task)

video_id = input("Enter the Video Id of the Youtube Video:\n eg : https://www.youtube.com/watch?v=1xg_aCtRtTU \n the ID for the above video is : 1xg_aCtRtTU")
yt = YouTubeTranscriptApi()
result = yt.get_transcript(video_id=video_id , languages=["en"])
# print(len(result))

# after loading the transcript we get a list of dict {"text" : " " , "start" : ,"duration": }
# we need to join these to form a single string

complete_transcript = " ".join(doc["text"] for doc in result)  # we join each text  to " " and finally get the entire document
# print(len(complete_transcript))

# DOCUMENT SPLITTER 

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)
doclist_transcript = splitter.create_documents([complete_transcript])

# print(len(doclist_transcript))

vectorStore = FAISS.from_documents(
    embedding=embedding_model,
    documents=doclist_transcript
)

# CREATING A RETRIEVER

retriever = vectorStore.as_retriever(search_type="mmr" , search_kwargs={"k" :4 , "lambda_mult" : 0.6})

# Creating Prompt
template = ChatPromptTemplate.from_messages([
    ("system","You are a You are a helpful assistant.\nAnswer ONLY from the provided transcript context. \nIf the context is insufficient, just say you don't know"),
    ("user","Context :\n{context}\n Query :\n{query}")
])

# OUTPUT PARSER
parser = StrOutputParser()

# chaining / Augmentation
parallel_chain = RunnableParallel({
    "query" : RunnablePassthrough(),
    "context" : retriever | RunnableLambda(lambda x:"\n\n".join(elem.page_content for elem in x))
})
seq_chain = template | model | parser
final_chain = parallel_chain|seq_chain

# Retrieval
while(True):
    query = str(input("Enter the Question : "))
    if(query.lower() == "exit"):
        break
    result = final_chain.invoke(query)
    print("AI : ",result)

print("\nIt was an Honor Serving You")