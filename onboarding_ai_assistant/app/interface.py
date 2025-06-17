# app/interface.py

import streamlit as st
from rag_pipeline import generate_answer

st.set_page_config(page_title="Asistente Onboarding AI")

st.title("🤖 Asistente de Onboarding")
st.markdown("Consulta manuales, políticas y FAQs de RRHH.")

query = st.text_input("¿En qué necesitas ayuda?")

if st.button("Buscar respuesta") and query:
    with st.spinner("Pensando..."):
        answer = generate_answer(query)
    st.success("✅ Respuesta generada:")
    st.write(answer)
