from src.vector_store import load_vector_store

db = load_vector_store()

query = "What skills does Aishwarya have?"

docs = db.similarity_search(query, k=2)

for i, doc in enumerate(docs, start=1):
    print(f"\n--- Result {i} ---\n")
    print(doc.page_content)