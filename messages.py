from langchain_core.messages import ChatMessage, SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from load_dotenv import load_dotenv

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant that provides concise and accurate answers to user questions."),
    HumanMessage(content="What is the capital of India?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)


