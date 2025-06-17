# app/embed_and_index.py

import os
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Paths absolutos desde la raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / 'data'
INDEX_FILE = BASE_DIR / 'faiss_index.index'
DOCS_FILE = BASE_DIR / 'docs.pkl'

# Modelo de embeddings
print("Cargando modelo...")
model = SentenceTransformer('all-MiniLM-L6-v2')

# Leer documentos y dividir en fragmentos
documents = []
sources = []

txt_files = list(DATA_DIR.glob("*.txt"))
if not txt_files:
    raise FileNotFoundError("No se encontraron archivos .txt en /data")

for file in txt_files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        chunks = [p.strip() for p in text.split('\n\n') if p.strip()]
        documents.extend(chunks)
        sources.extend([file.name] * len(chunks))

if not documents:
    raise ValueError("No hay fragmentos válidos en los textos.")

# Embeddings
embeddings = np.array(model.encode(documents))
if len(embeddings.shape) != 2:
    raise ValueError("Error al generar los embeddings: no tienen forma (n, d)")

# Crear índice FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Guardar
faiss.write_index(index, str(INDEX_FILE))
with open(DOCS_FILE, 'wb') as f:
    pickle.dump((documents, sources), f)

print(f"Indexado completo con {len(documents)} fragmentos.")
