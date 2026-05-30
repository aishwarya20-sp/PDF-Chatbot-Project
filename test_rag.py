from src.rag import ask_question

question = "What skills does Aishwarya have?"

answer = ask_question(question)

print("\nAnswer:\n")
print(answer)