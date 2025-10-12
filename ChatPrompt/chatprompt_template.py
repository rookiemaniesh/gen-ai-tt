from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
#not same as promptemplate
chat_template=ChatPromptTemplate([
    ('system',"you're a helpful assistant in this {domain}"),
    ('human',"give a brief idea about this {topic}")
])
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
prompt=chat_template.invoke({'domain':'cricket','topic':'sledging'})
# print(prompt)
result=model.invoke(prompt)
print(result.content)
