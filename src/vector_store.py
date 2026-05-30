from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(chunks):
    db = FAISS.from_texts(
        chunks,
        embedding_model
    )
    return db

def save_vector_store(db):
    db.save_local("faiss_index")

def load_vector_store():
    db = FAISS.load_local(
        "faiss_index",
        embedding_model,
        allow_dangerous_deserialization=True
    )
    return db