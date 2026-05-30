from src.pdf_loader import load_pdf, split_text

from src.vector_store import (
    create_vector_store,
    save_vector_store
)

pdf_path = "Aishwarya_Palase_26.pdf"   # use your PDF name

text = load_pdf(pdf_path)

chunks = split_text(text)

db = create_vector_store(chunks)

save_vector_store(db)

print("FAISS Index Created Successfully")