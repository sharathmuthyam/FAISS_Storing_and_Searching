# 🧠 Simple Nearest Vector Retrieval using FAISS (Terminal Version)

This project demonstrates a basic semantic retrieval system using FAISS for fast vector similarity search — designed to work entirely from the terminal, without relying on a language model.

---

## 📚 What It Does

- ✅ Loads a `.txt` knowledge base (e.g., school rules)
- ✅ Splits the content into chunks (e.g., 50 words each)
- ✅ Generates semantic vector embeddings using `sentence-transformers`
- ✅ Stores the vectors in a **FAISS** index
- ✅ Accepts user queries from the terminal
- ✅ Finds and prints the most semantically similar chunks

---

## 🧩 Files in This Repo

| File         | Purpose                                     |
|--------------|---------------------------------------------|
| `Rag1.py`    | Main script to build index and query it     |
| `text.txt`   | Input text file with content to search from |

---

## 🚀 How to Run

### 1. Install Requirements

```bash
pip install sentence-transformers faiss-cpu numpy
python3 Rag1.py

```
you will see:
🤖 Ask me anything about Rainbow School!
You: what is rainbow
📚 Top Relevant Chunks:
...


## 📅 Update: July 5, 2025 Rag_v1_basic.py

### 🔧 New Features / Commits Added:
- ✅ **Built an end-to-end RAG pipeline**
  - Uses `sentence-transformers` for embedding text chunks.
  - Stores and searches embeddings using **FAISS**.
- ✅ **Improved chunking strategy**
  - Rulebook text is now chunked by word count (default 50).
- ✅ **Integrated OpenAI GPT model** (or fallback to local Transformers)
  - GPT is prompted using top retrieved context chunks.
- ✅ **Threshold-based filtering of chunks** before prompting.
- ✅ **Fallback logic** added for when no relevant chunk is found.
- ✅ Logs and prints 🔍 retrieved chunks and final 🧠 answer.

### 🧪 Example Interaction:


👨‍💻 Created By
Sharath Chandra Reddy Muthyam
For learning how real-world AI engineers build semantic search and intelligent retrieval systems.

