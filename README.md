# 🤖 Onboarding AI Assistant

Un asistente conversacional basado en inteligencia artificial generativa y Recuperación de Información Aumentada (RAG) para facilitar el **proceso de incorporación de nuevos empleados** en una organización.

Este sistema responde de forma natural a preguntas sobre **manuales internos, políticas de empresa y FAQs de RRHH**, reduciendo la carga de trabajo de los departamentos de recursos humanos y mejorando la experiencia de los nuevos trabajadores.

---

## 🧠 ¿Qué es RAG?

**RAG (Retrieval-Augmented Generation)** es una técnica que combina:

- 🔍 Recuperación de información relevante (mediante embeddings + búsqueda vectorial)
- ✍️ Generación de respuestas con modelos de lenguaje (LLM)

En este proyecto:
- Se vectorizan documentos internos (manuales, políticas, etc.)
- Se indexan con FAISS
- Cuando un usuario hace una pregunta, se recuperan los fragmentos relevantes
- Y se genera una respuesta coherente con OpenAI GPT-3.5 o superior

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

## 🧠 Arquitectura del sistema RAG

```text
┌────────────────────────────┐
│     Documentos internos    │
│  (manuales, políticas, FAQ)│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ División en fragmentos     │
│ (chunks de texto)          │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Embeddings con MiniLM      │
│ (sentence-transformers)    │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Almacenamiento en FAISS    │
│ (índice vectorial)         │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│   Usuario hace una         │
│   pregunta en lenguaje nat.│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Embedding de la pregunta   │
│ + búsqueda semántica       │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Recuperación de fragmentos │
│ más relevantes (top-k)     │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│   Generación del prompt    │
│ con contexto + pregunta    │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ LLM (GPT-4) genera respuesta│
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│    Respuesta mostrada en   │
│       Streamlit UI         │
└────────────────────────────┘
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
$env:OPENAI_API_KEY="tu_clave_aquí"
```

### 5. Genera el índice vectorial

```bash
python embed_and_index.py
```

### 6. Lanza la aplicación web

```bash
streamlit run interface.py
```

---

## 💬 Ejemplos de preguntas
¿Cuántos días de vacaciones tengo al año?
¿Puedo coger vacaciones durante el periodo de prueba?
¿Dónde solicito mis vacaciones?
¿Puedo acumular días no disfrutados?
¿Con cuánta antelación debo avisar para las vacaciones?

---

## ⚠️ Limitaciones y futuras mejoras

### 🔍 Limitaciones actuales

- **Cobertura limitada de datos**: El sistema solo responde sobre los documentos cargados manualmente. No accede en tiempo real a bases dinámicas (como SharePoint o intranets).
- **Dependencia del lenguaje**: Está optimizado para textos y preguntas en español, pero puede fallar si se mezcla con otros idiomas o jergas no documentadas.
- **Modelo externo (GPT-4)**: El uso de OpenAI requiere conexión a internet y una API Key. No es completamente autónomo ni privado.
- **Sin gestión de usuarios ni autenticación**: Cualquier persona que acceda a la interfaz puede hacer preguntas. No hay personalización del contenido según el perfil del empleado.
- **Costes asociados**: Cada pregunta enviada al modelo generativo (GPT-4) tiene un coste si se usa la API comercial.

---

### 🚀 Posibles mejoras futuras

- **Integración con bases de datos reales de RRHH**: Conexión a portales internos, wikis corporativas o gestores documentales para mantener la información actualizada.
- **Mejor control de acceso**: Añadir login, perfilado de empleados y filtrado de respuestas según rol (interno, externo, becario...).
- **Respuestas multilingües**: Ampliar la capacidad del sistema para responder en varios idiomas dependiendo del idioma de la pregunta.
- **Sustitución de GPT-4 por modelos open source**: Migración a Llama 3 o Mixtral para eliminar la dependencia de servicios externos y garantizar privacidad.
- **Evaluación automática de calidad**: Añadir métricas de precisión o feedback de usuario para mejorar continuamente el sistema.

---

