# 🎥 YouTube Transcript Chatbot  

An **AI-powered chatbot** that allows users to query a YouTube video’s transcript and receive precise answers.  

---

## 🔹 Features  

✅ **Automatic Transcript Fetching** – Extracts subtitles using [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/).  
✅ **Text Chunking & Storage** – Splits transcript into manageable chunks using LangChain’s `RecursiveCharacterTextSplitter`.  
✅ **Vector Database** – Stores embeddings in **FAISS** for efficient semantic search.  
✅ **Context-Aware Retrieval** – Uses **MMR-based retriever** to fetch the most relevant transcript chunks.  
✅ **LLM-Powered Responses** – Answers queries using **llama3.1** via Ollama, restricted to transcript context.  
✅ **Interactive CLI Chatbot** – Ask questions in real-time; exit anytime with `"exit"`.  

---

## 🛠️ Tech Stack  

- **LangChain** – Orchestration & prompt management  
- **Ollama** – LLaMA 3.1 model for natural language responses  
- **FAISS** – Vector database for transcript retrieval  
- **youtube-transcript-api** – Fetching video transcripts  

---

## 🚀 How It Works  

1. Extract transcript from a YouTube video.  
2. Preprocess & chunk the transcript into smaller sections.  
3. Store embeddings in a **FAISS vectorstore**.  
4. Retrieve relevant context chunks for each query.  
5. Generate context-aware responses using the LLM.  

---

## 📦 Installation  

Clone the repository and install dependencies:  

```bash
git clone https://github.com/your-username/youtube-transcript-chatbot.git
cd youtube-transcript-chatbot

pip install -r requirements.txt

