from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a restuarant.
Here are some relevant reviews: {reviews}
Given the reviews, answer the question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model



while True:
    question = input("Enter a question about the restaurant: ")
    print("\n")
    if question == "exit":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke( {
        "reviews": reviews, "question": question})
    print(result)