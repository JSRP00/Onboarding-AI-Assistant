# 🤖 Onboarding AI Assistant

Este proyecto consiste en un **asistente inteligente basado en Recuperación de Información Aumentada (RAG)** que facilita el acceso rápido a información clave durante el proceso de incorporación de nuevos empleados. Utiliza técnicas de IA generativa y búsqueda semántica para responder preguntas en lenguaje natural a partir de documentos internos de RRHH.

---

## 📌 Objetivo

Reducir la carga del equipo de Recursos Humanos y mejorar la experiencia del nuevo empleado permitiéndole consultar directamente información clave (vacaciones, políticas, horarios, beneficios, etc.) mediante una interfaz conversacional inteligente.

---

## 🛠️ Tecnologías utilizadas

- `sentence-transformers`: para generar embeddings semánticos.
- `FAISS`: índice vectorial para búsqueda de fragmentos relevantes.
- `OpenAI GPT-4`: para generación de respuestas en lenguaje natural.
- `Streamlit`: interfaz web para interacción con el asistente.

---

## 📁 Estructura del proyecto

```text
onboarding-ai-assistant/
│
├── data/
│   ├── manual_bienvenida.txt
│   ├── politica_vacaciones.txt
│   └── faq_rrhh.txt
│
├── app/
│   ├── embed_and_index.py       # Vectorización e indexado
│   ├── rag_pipeline.py          # Búsqueda + generación
│   └── interface.py             # Interfaz con Streamlit
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalación y uso

### 1. Clona este repositorio

```bash
git clone https://github.com/JSRP00/onboarding-ai-assistant.git
cd onboarding-ai-assistant
```

### 2. (Opcional) Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Añade tu clave de OpenAI como variable de entorno

```bash
# En Linux/macOS
export OPENAI_API_KEY="tu_clave_aquí"

# En Windows CMD
set OPENAI_API_KEY=tu_clave_aquí
```

### 5. Genera el índice vectorial

```bash
python app/embed_and_index.py
```

### 6. Lanza la aplicación web

```bash
streamlit run app/interface.py
```
