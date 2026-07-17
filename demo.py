# Import required libraries
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM


# Streamlit App Title
st.title("LangChain + Ollama DeepSeek Chat App")


# Prompt Template
template = """
You are a helpful AI assistant.

Question: {question}

Answer:
"""

prompt = ChatPromptTemplate.from_template(template)


# Ollama Model
# First install model:
# ollama pull deepseek-r1

model = OllamaLLM(
    model="deepseek-r1:1.5b"
)

chain = prompt | model


# User Input
question = st.chat_input("Enter your question here")


# Generate Response
if question:

    st.chat_message("user").write(question)

    with st.chat_message("assistant"):
        response = chain.invoke(
            {
                "question": question
            }
        )

        st.write(response)