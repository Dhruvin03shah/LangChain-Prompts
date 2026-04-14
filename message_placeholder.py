from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that provides concise and accurate answers to user questions."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{query}?")
])

chat_history = []
# chat history

with open("chat_history.txt", "r") as f:
    chat_history.extend(f.read().splitlines())

# create prompt

chat_template.invoke({'Chat_History': chat_history, 'query': "Where is my refund?"})

print(prompt)
