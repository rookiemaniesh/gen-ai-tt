from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#You’re getting ValueError: no signature found for builtin type <class 'dict'> because with_structured_output() doesn’t support plain TypedDict — it expects a Pydantic model or function with a defined signature. The quick fix is to replace your TypedDict with a Pydantic BaseModel.
class Review(BaseModel):
    summary:str
    sentiment:str

structed_model=model.with_structured_output(Review)
result=structed_model.invoke('the hardware is great everything feels fine, but need an update in software a bit laggy ')
# print(result)
print(result.sentiment)
