"""
Demonstrates how to use the Langchain Anthropic model
with the Langchain OpenAPI agent toolkit.
"""

import os
import json
import argparse

from langchain_community.utilities.requests import RequestsWrapper
from langchain_community.agent_toolkits.openapi import planner
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain_anthropic import ChatAnthropic

# Set to True to allow dangerous requests
# (e.g. requests that modify data or perform actions)
ALLOW_DANGEROUS_REQUEST = True

# Make sure we have the Anthropic API key environment variable set
if "ANTHROPIC_API_KEY" not in os.environ:
    raise ValueError("ANTHROPIC_API_KEY environment variable not set")

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "query", type=str, help="User query. E.g: 'Who won in Monaco in 2024?'"
)
argparser.add_argument(
    "--model", type=str, default="claude-3-sonnet-20240229", help="Model name"
)
argparser.add_argument("--timeout", type=int, default=10, help="Timeout in seconds")
argparser.add_argument("--stop", type=str, default="</s>", help="Stop token")
args = argparser.parse_args()

user_query = (args.query,)

model = ChatAnthropic(
    model_name=args.model,
    timeout=args.timeout,
    stop=[
        args.stop,
    ],
)

with open("openapi.json") as f:
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

f1_agent.invoke(messages)
