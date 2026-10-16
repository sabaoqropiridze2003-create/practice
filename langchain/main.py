# from dotenv import load_dotenv
# load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate

# MODEL_NAME = "gemini-3.5-flash-lite"

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

#################################################################
# practice
#################################################################


# result = model.invoke("what is the capital of france?")
# print(result.text)

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "You are a helpfull {subject} assistant"),
#         ("human", "{question}"),
#     ]
# )

# prompt_input = prompt.invoke(
#     {
#         "subject": "Python",
#         "question": "when was python created?"
#     }
# )

# print(prompt_input)

# response = model.invoke(prompt_input)

# print(response.text)

# chain = prompt | model

# response = chain.invoke(
#     {
#         "subject": "Python",
#         "question": "when was python created?"        
#     }
# )

# print(response.text)


#################################################################
# Output Parsers
#################################################################

## StrOutputParser ##

# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# from dotenv import load_dotenv
# load_dotenv()

# MODEL_NAME="gemini-3.5-flash-lite"

# model = ChatGoogleGenerativeAI(
#     model=MODEL_NAME
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", "you are a helpfull {subject} assistant"),
#         ("human", "{question}"),
#     ]
# )

# parser = StrOutputParser()

# chain = prompt | model | parser

# user_question = input("enter your question: ")

# response = chain.invoke(
#     {
#         "subject": "geography",
#         "question": user_question
#     }
# )

# print(response)

## PydanticOutputParser ##

from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

MODEL_NAME = "gemini-3.5-flash-lite"

model = ChatGoogleGenerativeAI(
    model=MODEL_NAME
)

class ProductReview(BaseModel):
    score: int = Field(ge=1, le=10)
    coment: str = Field(min_length=10)
    recommend: bool

parser = PydanticOutputParser(pydantic_object=ProductReview)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
        you are a helpfull asistant, analize following car review and provide
        - a raiting from 1 to 10
        - a short summary
        - whether you recomend the car

        {format_instructions}
        """),

        ("human", "{car_review}"),
    ]
)

chain = prompt | model | parser

response = chain.invoke(
    {
        "format_instructions": parser.get_format_instructions(),
        "car_review": "car is in good condition, but it is old, it was produced in 2003."
    }
)

for key, value in response.model_dump().items():
    print(f"{key}: {value}")






