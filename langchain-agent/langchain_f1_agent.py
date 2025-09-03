import json
import time

from langchain_community.utilities.requests import RequestsWrapper
from langchain_community.agent_toolkits.openapi import planner
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from config.llm import LlmService

# Set to True to allow dangerous requests
# (e.g. requests that modify data or perform actions)
ALLOW_DANGEROUS_REQUEST = True

model = LlmService.get_model(model_name="gpt-4o-mini")

class F1_Agent:
    @classmethod
    def get_api_response(cls, query):
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
        tic = time.perf_counter()
        response = f1_agent.invoke(messages)
        toc = time.perf_counter()
        print("===============================================================")
        print(f"=== DONE: invoke the agent - {toc - tic:0.4f} seconds ==========")
        print("===============================================================")

        return response

