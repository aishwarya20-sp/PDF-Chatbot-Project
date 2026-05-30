from src.pdf_loader import load_pdf, split_text

pdf_path = "Aishwarya_Palase_26.pdf"   # replace with your actual PDF name

text = load_pdf(pdf_path)

chunks = split_text(text)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])

print("\nSecond Chunk:\n")
print(chunks[1])