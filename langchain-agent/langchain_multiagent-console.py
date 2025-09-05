import os
import argparse
from langchain_agent import LangChainAgent

os.system('cls' if os.name == 'nt' else 'clear')

f1_system_context = "Answer the F1 query using the API. Race names with two words should be separated by an underscore and be in lowercase. The API stores data from 2021 to 2024."
f1_openapi_json_file = "openapi-f1.json"

policy_system_context = "Answer the Insurance Policy query using the API. Stamp References should be in full and be in uppercase. The API stores data from 2021 to 2025."
policy_openapi_json_file = "openapi-policy.json"

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "query", type=str, help="User query. E.g: 'Who won in Monaco in 2024?'"
)
args = argparser.parse_args()
user_query = (args.query,)

def main():
    response = LangChainAgent.get_api_response(query=user_query, 
                                            openapi_json_file=f1_openapi_json_file,
                                            system_context=f1_system_context)
    print(response['output'])
                
#Invoking main function
if __name__ == '__main__':
    main()
