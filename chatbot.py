from langchain_openai import ChatOpenAI
from langchain_core.messages import ChatMessage, SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to user questions."),
]

while True:
    user_input = input("Enter your question (or 'exit' to quit): ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("Chatbot:", response.content)     

    print("\nChat History:")