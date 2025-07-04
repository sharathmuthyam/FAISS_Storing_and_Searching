# 1. Imports
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 2. Load and chunk rulebook
def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

with open("/Users/sharath_muthyam/Desktop/text.txt", "r", encoding="utf-8", errors="ignore") as f:
    full_text = f.read()

chunks = chunk_text(full_text, chunk_size=50)

# 3. Embed chunks and store in FAISS
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)
vectors = np.array(embeddings)

dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(vectors)

# 4. Search function
def search_chunks(query, model, index, chunks, top_k=3):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    return [chunks[i] for i in indices[0]]

# 5. Interactive terminal loop
print("🤖 Ask me anything about Rainbow School!")
while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    results = search_chunks(query, model, index, chunks)
    print("\n📚 Top Relevant Chunks:")
    for i, r in enumerate(results):
        print(f"\n[{i+1}] {r}")
