# app/rag_pipeline.py

import faiss
import pickle
from pathlib import Path
from sentence_transformers import SentenceTransformer
from openai import OpenAI
import os

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_FILE = BASE_DIR / 'faiss_index.index'
DOCS_FILE = BASE_DIR / 'docs.pkl'

# API key de OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY no está definido como variable de entorno.")
openai = OpenAI(api_key=api_key)

# Cargar datos
index = faiss.read_index(str(INDEX_FILE))
with open(DOCS_FILE, 'rb') as f:
    documents, sources = pickle.load(f)

# Cargar modelo
model = SentenceTransformer('all-MiniLM-L6-v2')

# Función de búsqueda
def search(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    results = [f"[{sources[i]}] {documents[i]}" for i in indices[0]]
    return "\n".join(results)

# Función de respuesta generada
def generate_answer(query):
    context = search(query)
    prompt = f"Responde a la pregunta usando solo la información:\n\n{context}\n\nPregunta: {query}\nRespuesta:"
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
