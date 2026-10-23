from dotenv import load_dotenv
load_dotenv() 

from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI

MODEL = "gemini-3.5-flash-lite"

class State(TypedDict):
    text: str
    detected_language: str
    translated_text: str

def detect_language(state: State):

    llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

    prompt = f"""
    you are a language detection model. detect the language of the following text
    {state['text']}
    return only the language name!
    """

    response = llm.invoke(prompt)

    return {
        "detected_language": response.text
    }

def translate_text(state: State):

    llm = ChatGoogleGenerativeAI(
        model=MODEL
    )

    prompt = f"""
    you are a translation model, translate the following text in georgian
    {state['text']}
    return only the translated text!
    """

    response = llm.invoke(prompt)

    return {
        "translated_text": response.text
    }

builder = StateGraph(State)

builder.add_node("detect", detect_language)
builder.add_node("translate", translate_text)


builder.add_edge(START, "detect")
builder.add_edge("detect", "translate")
builder.add_edge("translate", END)

graph = builder.compile()

while True:
    input_text = input("please enter your text: ")

    if input_text.lower() in ["quit", "exit"]:
        break

    result = graph.invoke({
        "text": input_text
    })

    print(f"detected language: {result.get("detected_language", "can not detect the language")}")
    print(f"translated text: {result.get("translated_text", "can not translate the text")}")

