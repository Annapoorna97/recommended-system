# build a Recommender System...
import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# import local environment
from dotenv import load_dotenv
load_dotenv()
import os
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Design the Page... streamlit run app.py
headers = {"authorization":st.secrets["GOOGLE_API_KEY"],
           "content-type":"application/json"}

st.title("Movie Recommender System...")
user_input = st.text_input("Enter the Movie title,genre or Keyword")

#prompt Template 
demo_template = ''' Based on {user_input} provide movie Recommendations'''
template = PromptTemplate(input_variables =["user_input"],template = demo_template)



# google gemini model 
llm = ChatGoogleGenerativeAI(model = 'gemini-pro',api_key='GOOGLE-API-KEY')
if user_input:
    prompt = template.format(user_input = user_input)
    recommendations = llm.predict(text=prompt)
    st.write(f"Recommendations for you:\n {recommendations}")
else:
    st.write("")


# streamlit run app.py
 