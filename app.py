import streamlit as st
from src.rag import ask_question

st.set_page_config(page_title="PDF Chatbot")

st.title("📄 PDF Chatbot")

question = st.text_input("Ask a question about the PDF")

if st.button("Ask"):

    answer = ask_question(question)

    st.write("### Answer")
    st.write(answer)