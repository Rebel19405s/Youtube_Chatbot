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

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/youtube-transcript-chatbot.git
cd youtube-transcript-chatbot
```
### 2️⃣ Install Python Dependencies

Create a virtual environment first.
```bash
pip install -r requirements.txt
```
### 3️⃣ Install Ollama

Go to the Ollama website and download Ollama for your system.
link : (https://ollama.com/download)
After installing, open Command Prompt / Terminal and run the following commands:

```bash
ollama run llama3.1
ollama run nomic-embed-text
```

This will install:

llama3.1 → the chat model used for answering questions

nomic-embed-text → the embedding model used for vector storage

After installation, close the command prompt.

### ▶️ Usage

Run the chatbot with:
```bash
python main.py
```

Ask your questions interactively. Type exit anytime to quit.

### 📂 Project Structure
📦 youtube-transcript-chatbot
 ┣ 📜 main.py              # Entry point for chatbot
 ┣ 📜 requirements.txt     # Dependencies
 ┣ 📜 README.md 
