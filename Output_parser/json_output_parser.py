from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser=JsonOutputParser()

template=PromptTemplate(
    template='give the name age city of the fictional character\n,{format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)
prompt=template.format()
# result=model.invoke(prompt)
# # print(result)
# final_result=parser.parse(result.content)
# print(final_result)

chain= template | model | parser
result=chain.invoke({}) #input variable khali hai iss liye 
print(result)

# dekha schema validation nhi hai isme
# Invalid json output: Please provide me with the name of the fictional character you'd like the information for! 😉

# Once I know the character's name, I can give you their age and city.

# For example, you could say:

# "Give the name, age, and city of the fictional character **Atticus Finch**."

# Then, I'll give you the answer in JSON format. 😊
