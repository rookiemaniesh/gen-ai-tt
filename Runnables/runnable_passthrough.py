# ye kuch nhi krta hai isme jo daalo whi bhr kr dega 
# ek use case niche h

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
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

joke_geneerator=RunnableSequence(prompt1,model,parser)

parallel=RunnableParallel({
    'joke':RunnablePassthrough(),
    'meaning':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_geneerator,parallel)
result=final_chain.invoke({'topic':'a boy named rajveer'})
print(result['joke'])
print(result['meaning'])


