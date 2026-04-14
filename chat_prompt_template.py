# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import ChatMessage, SystemMessage, HumanMessage, AIMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} assistant that provides concise and accurate answers to user questions."),
#     HumanMessage(content="Explain in simple terms what is {topic}")
# ]) 

# prompt = chat_template.invoke(domain="math", topic="calculus") 

# print(prompt)





## IMPORTANT NOTE: 

# The above code is just to demonstrate the concept of chat prompt template. It is not used in the actual implementation of the UI.

# --we use this because chatprompttemplate inlangchain does not work like promptTemplate and it does not have the save and load functionality. So we create a prompt template using prompttemplate and then save it and load it in the ui file.


from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant that provides concise and accurate answers to user questions."),
    ('human', "Explain in simple terms what is {topic}")
])

prompt = chat_template.invoke(domain="math", topic="calculus") 

print(prompt)







