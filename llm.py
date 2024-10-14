import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import streamlit as st
from graph import graph

load_dotenv()


# Create the LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             google_api_key=st.secrets["GOOGLE_API_KEY"] 
                             )

# Create the Embedding model
