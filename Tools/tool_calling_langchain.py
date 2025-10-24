from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
load_dotenv()

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
@tool
def multiply(a:int,b:int)->int:
    """it multiply the two numbers"""
    return a*b
# print(multiply.invoke({'a':3,"b":3}))

# binding tool with llm
llm_with_tools=llm.bind_tools([multiply])
# result=llm_with_tools.invoke('Hi How are you?')
# print(result)
query = HumanMessage('can you multiply 3 with 1000')
messages=[query]
result=llm_with_tools.invoke(messages)
messages.append(result)
# print(messages)
tool_result = multiply.invoke(result.tool_calls[0])
print(tool_result)
final_result=llm_with_tools.invoke(messages).content
print(final_result)
