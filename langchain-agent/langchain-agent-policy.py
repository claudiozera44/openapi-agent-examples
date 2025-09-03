import os
import json
import openai
import argparse
from dotenv import find_dotenv, load_dotenv

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
    with open("openapi-policy.json") as f:
        openapi = json.load(f)
    requests_wrapper = RequestsWrapper()
    policy_spec = reduce_openapi_spec(openapi)
    policy_agent = planner.create_openapi_agent(
        policy_spec, requests_wrapper, model, allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST
    )
    messages = [  
        ("system", "Answer the Insurance Policy query using the API. Stamp References should be in full and be in uppercase. The API stores data from 2021 to 2025."),  
        ("human", user_query),  
    ]  
    response = policy_agent.invoke(messages)
    return response

def main():
    query = "Who is the client for stamp ref. P25R0934458M year 2025?"
    os.system('cls' if os.name == 'nt' else 'clear')
    response = get_api_response(query=query)
    print(response['output'])
                
#Invoking main function
if __name__ == '__main__':
    main()
