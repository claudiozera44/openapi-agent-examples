import os
import argparse
from langchain_agent import LangChainAgent

os.system('cls' if os.name == 'nt' else 'clear')

system_context = "Answer the Insurance Policy query using the API. Stamp References should be in full and be in uppercase. The API stores data from 2021 to 2025."
openapi_json_file = "openapi-policy.json"
argparser = argparse.ArgumentParser()
argparser.add_argument(
    "query", type=str, help="User query. E.g: 'Who is the client for stamp ref. P25R0934458M year 2025?'"
)
args = argparser.parse_args()
user_query = (args.query,)

def main():
    response = LangChainAgent.get_api_response(query=user_query, 
                                            openapi_json_file=openapi_json_file,
                                            system_context=system_context)
    print(response['output'])
                
#Invoking main function
if __name__ == '__main__':
    main()
