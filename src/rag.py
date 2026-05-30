from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from src.vector_store import load_vector_store

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

db = load_vector_store()


def ask_question(question):

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content