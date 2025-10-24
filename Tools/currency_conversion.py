from langchain_core.tools import InjectedToolArg
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from dotenv import load_dotenv
from typing import Annotated
import requests

load_dotenv()

@tool 
def Conversion_rate(base_currency:str,target_currency:str)->float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url="https://v6.exchangerate-api.com/v6/93547c4445c0a7370c00a7d6/pair/{base_currency}/{target_currency}"
    response=requests.get(url)
    return response.json

@tool 
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
  """
  given a currency conversion rate this function calculates the target currency value from a given base currency value
  """

  return base_currency_value * conversion_rate

# Conversion_rate.invoke({'base_currency':'USD','target_currency':'INR'})
llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
llm_with_tools = llm.bind_tools([Conversion_rate, convert])
messages = [HumanMessage('What is the conversion factor between INR and USD, and based on that can you convert 10 inr to usd')]
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
# print(ai_message.tool_calls)
import json

for tool_call in ai_message.tool_calls:
  # execute the 1st tool and get the value of conversion rate
  if tool_call['name'] == 'get_conversion_factor':
    tool_message1 = Conversion_rate.invoke(tool_call)
    # fetch this conversion rate
    conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
  # execute the 2nd tool using the conversion rate from tool 1
  if tool_call['name'] == 'convert':
    # fetch the current arg
    tool_call['args']['conversion_rate'] = conversion_rate
    tool_message2 = convert.invoke(tool_call)
    messages.append(tool_message2)

print(messages)
# print(llm_with_tools.invoke(messages).content)
