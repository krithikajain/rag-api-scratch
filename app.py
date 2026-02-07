import os
from fastapi import FastAPI
import chromadb

# Mock LLM mode for CI testing
USE_MOCK_LLM = os.getenv("USE_MOCK_LLM", "0") == "1"

if not USE_MOCK_LLM:
    import ollama

app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

@app.post("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    if USE_MOCK_LLM:
        # In mock mode, return the retrieved context directly
        return {"answer": context}

    # In production mode, use Ollama
    answer = ollama.generate(
        model="tinyllama",
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}

# app = FastAPI()
# chroma = chromadb.PersistentClient(path="./db")
# collection = chroma.get_or_create_collection("docs")
# # ollama_client = ollama.Client(host="http://host.docker.internal:11434")
# ollama_client = ollama.Client(host='http://127.0.0.1:11434')

# @app.post("/query")
# def query(q: str):
#     results = collection.query(query_texts=[q], n_results=1)
#     context = results["documents"][0][0] if results["documents"] else ""

#     answer = ollama_client.generate(
#         model="tinyllama",
#         prompt=f"Context:\n{context}\n\nQuestion:\n{q}\n\nAnswer clearly and concisely"
#     )

#     return {"answer": answer["response"]}

# @app.post("/add")
# def add_knowledge(text: str):
#     """Add new content to the knowlege base dynamically."""
#     try:
#         #generate a unique id for the document
#         import uuid
#         doc_id = str(uuid.uuid4())
        
#         #add the text to the chroma collection
#         collection.add(documents=[text], ids=[doc_id])

#         return {
#             "status": "success",
#             "message": "Document added to knowledge base",
#             "id": doc_id
#         }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e)
#         }