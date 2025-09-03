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

class LangChainAgent:
    @classmethod
    def get_api_response(cls, query: str, 
                         openapi_json_file: str,
                         system_context: str):
        user_query = (query)
        with open(openapi_json_file) as f:
            openapi = json.load(f)
        requests_wrapper = RequestsWrapper()
        spec = reduce_openapi_spec(openapi)
        agent = planner.create_openapi_agent(
            spec, requests_wrapper, model, allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST
        )
        messages = [  
            ("system", system_context),  
            ("human", user_query),  
        ]  
        tic = time.perf_counter()
        response = agent.invoke(messages)
        toc = time.perf_counter()
        print("===============================================================")
        print(f"=== DONE: invoke the agent - {toc - tic:0.4f} seconds ==========")
        print("===============================================================")

        return response

