from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='tell me a funny joke on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain this joke- {text}',
    input_variables=['text']
)

parser=StrOutputParser()

chain=RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result=chain.invoke({'topic':'tech nerds'})
print(result)
