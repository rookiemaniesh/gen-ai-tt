from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage

from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
chatTemplate=ChatPromptTemplate([
    ('system','you are helpful ai assistant of ecommerce website that sells flowers'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{qwery}')
])
chat_history=[]
with open('ChatPrompt\chat_history.txt') as f:
    chat_history.extend(f.readlines())
# print(chat_history)
prompt=chatTemplate.invoke({'chat_history':chat_history,'qwery':'when will my flowers arrive?'})
# print(prompt)
result=model.invoke(prompt)
chat_history.append(f"AI: {result.content}")
print(result.content)
with open('ChatPrompt/chat_history.txt', 'a') as f:
    f.write(f"AI: {result.content}")
print(chat_history)