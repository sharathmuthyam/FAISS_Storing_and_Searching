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
👨‍💻 Created By
Sharath Chandra Reddy Muthyam
For learning how real-world AI engineers build semantic search and intelligent retrieval systems.

