🎥 YouTube Transcript Chatbot

An AI-powered chatbot that allows users to query a YouTube video’s transcript and receive precise answers.

🔹 Features

✅ Automatic Transcript Fetching – Extracts subtitles using youtube-transcript-api.
✅ Text Chunking & Storage – Splits transcript into manageable chunks using LangChain’s RecursiveCharacterTextSplitter.
✅ Vector Database – Stores embeddings in FAISS for efficient semantic search.
✅ Context-Aware Retrieval – Uses MMR-based retriever to fetch the most relevant transcript chunks.
✅ LLM-Powered Responses – Answers queries using llama3.1 via Ollama, restricted to transcript context.
✅ Interactive CLI Chatbot – Ask questions in real-time; exit anytime with "exit".

🛠️ Tech Stack

LangChain – Orchestration & prompt management

Ollama – LLaMA 3.1 model for natural language responses

FAISS – Vector store for transcript retrieval

youtube-transcript-api – Fetching video transcripts

🚀 How It Works

Extract transcript from a YouTube video.

Preprocess & chunk the transcript.

Store embeddings in a FAISS vector store.

Retrieve relevant context for each query.

Generate responses using an LLM constrained by transcript context.
