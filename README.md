# Onboarding AI Assistant

Retrieval-augmented generation (RAG) assistant that answers new employees' questions from internal HR documents: welcome manual, holiday policy and HR FAQ. Built as a course project in generative AI (MSc in Big Data Science, University of Navarra).

The sample documents and the answers are in Spanish.

## How it works

1. **Indexing** (`app/embed_and_index.py`): each document is split into paragraph chunks, embedded with `all-MiniLM-L6-v2` (sentence-transformers) and stored in a FAISS index.
2. **Retrieval** (`app/rag_pipeline.py`): the question is embedded and the three closest chunks are retrieved, together with their source file.
3. **Generation**: the chunks and the question go to an OpenAI chat model (`gpt-3.5-turbo`, temperature 0.2), instructed to answer only from that context.
4. **Interface** (`app/interface.py`): Streamlit web app.

## Run it

```bash
git clone https://github.com/JSRP00/Onboarding-AI-Assistant.git
cd Onboarding-AI-Assistant/onboarding_ai_assistant
pip install -r requirements.txt

export OPENAI_API_KEY="your-key"     # Windows PowerShell: $env:OPENAI_API_KEY="your-key"
python app/embed_and_index.py         # build the index
streamlit run app/interface.py
```

Example questions: *¿Cuántos días de vacaciones tengo al año?* · *¿Puedo coger vacaciones durante el periodo de prueba?* · *¿Dónde solicito mis vacaciones?*

## Limitations

- Answers only cover the documents in `data/`.
- Requires the OpenAI API (internet access and per-query cost); an open-source model would remove that dependency.
- No authentication or role-based filtering.
- No automatic evaluation of answer quality yet.
