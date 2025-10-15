from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='write a catchy tweet on this trending topic- {topic} ',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='write a eye catchy and professional short linkedin post on topic- {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1,model,parser),
        'linkedin':RunnableSequence(prompt2,model,parser)
    }
)
result=parallel_chain.invoke({'topic':'google new breaktrough in AI'})
print(result['tweet'])
print(result['linkedin'])