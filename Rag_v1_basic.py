from sentence_transformers import SentenceTransformer
from transformers import pipeline
import faiss
from openai import OpenAI
import numpy as np
import openai

client = OpenAI(api_key="#  Replace with your API key")  

# 1. Load and chunk the rulebook
def chunk_text(text, chunk_size=50):
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

with open("/Users/sharath_muthyam/Desktop/text.txt", "r", encoding="utf-8", errors="ignore") as f:
    full_text = f.read()

chunks = chunk_text(full_text, chunk_size=50)

# 2. Embed with sentence-transformers
model = SentenceTransformer('all-MiniLM-L6-v2')
vectors = np.array(model.encode(chunks))
dimension = vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(vectors)

# 3. Search top-k relevant chunks
def search_chunks(query, model, index, chunks, top_k=3, threshold=1.5):
    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), top_k)
    
    
    return [chunks[i] for i in indices[0]]


# 4. Use LLM to generate final answer
'''def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""You are an assistant for Rainbow School. Answer the question based only on the following information:\n\n{context}\n\nQuestion: {query}\nAnswer: if you don't know the answer, say "I don't know"."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response.choices[0].message.content'''
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)

    try:
        result = qa_pipeline(question=query, context=context)

        # If no answer found
        if not result or result['answer'].strip() == "":
            return "I don't know."

        # Fix: strip and return as a string
        return str(result['answer']).strip()

    except Exception as e:
        return f" Error: {str(e)}"

# 5. Terminal loop
print(" Ask me anything about Rainbow School (type 'exit' to quit)")
while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit"]:
        print(" Goodbye!")
        break

    relevant_chunks = search_chunks(query, model, index, chunks)
    if not relevant_chunks:
        print(" Sorry, I couldn’t find relevant info.")
    else:
        print(f"\n Relevant chunks:\n{relevant_chunks}")
        print(context := "\n".join(relevant_chunks))  # Print context for debugging
        answer = generate_answer(query, relevant_chunks)
        print(f"\n Answer:\n{answer}")
