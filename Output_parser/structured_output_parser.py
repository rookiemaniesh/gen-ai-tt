from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema=[
    ResponseSchema(name='fact1',description='first fact about the topic'),
    ResponseSchema(name='fact2',description='second fact about the topic'),
    ResponseSchema(name='fact3',description='third fact about the topic')
]
parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template='give me three facts about {topic},\n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)
# prompt=template.invoke({'topic':'generative AI'})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)

chain= template | model | parser
result=chain.invoke({'topic':'Generative AI'})
print(result)