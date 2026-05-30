from src.pdf_loader import load_pdf

pdf_path = "Aishwarya_Palase_26.pdf"

text = load_pdf(pdf_path)

print(text[:500])