#koi bhi pyhton function ko runnable bana dega 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt1=PromptTemplate(
    template='tell me a funny joke on {topic}',
    input_variables=['topic']
)

def word_count(text):
    return len(text.split())

parser=StrOutputParser()

joke_geneerator=RunnableSequence(prompt1,model,parser)

parallel=RunnableParallel({
    'joke':RunnablePassthrough(),
    'count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(joke_geneerator,parallel)
result=final_chain.invoke({'topic':'virat kohli'})
print(result['joke'])
print(result['count'])


