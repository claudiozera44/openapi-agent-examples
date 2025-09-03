import os
import json
import openai
from dotenv import find_dotenv, load_dotenv
import streamlit as st 

from langchain_openai.llms import OpenAI
from langchain_community.utilities.requests import RequestsWrapper
from langchain_community.agent_toolkits.openapi import planner
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec

# Set to True to allow dangerous requests
# (e.g. requests that modify data or perform actions)
ALLOW_DANGEROUS_REQUEST = True

os.system('cls' if os.name == 'nt' else 'clear')

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

model = OpenAI(temperature=0.7, model="gpt-4o-mini")

def get_api_response(query):
    user_query = (query)
    with open("openapi-f1.json") as f:
        openapi = json.load(f)
    requests_wrapper = RequestsWrapper()
    f1_spec = reduce_openapi_spec(openapi)
    f1_agent = planner.create_openapi_agent(
        f1_spec, requests_wrapper, model, allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST
    )
    messages = [  
        ("system", "Answer the F1 query using the API. Race names with two words should be separated by an underscore and be in lowercase. The API stores data from 2021 to 2024."),  
        ("human", user_query),  
    ]  
    response = f1_agent.invoke(messages)
    return response

def main():
    st.title("F1 OpenAPI Agent")
    st.set_page_config(page_title="F1 OpenAPI Agent",
                       layout="centered")
    st.title("Let AI find answers for You 📖")
    st.header("Get Started...")
    
    query = st.text_input(label="What's your query?", value="Who won in Monaco in 2024?")
    
    submit_button = st.button("Submit")
    if query:
        if submit_button:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            with st.spinner("Processing..."):
                response = get_api_response(query=query)
                
                with st.expander("response"):
                    st.write(response['output'])
                
            st.success("Response has been provided!")

#Invoking main function
if __name__ == '__main__':
    main()  