import os
import argparse
from langchain_policy_agent import PolicyAgent

os.system('cls' if os.name == 'nt' else 'clear')

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "query", type=str, help="User query. E.g: 'Who is the client for stamp ref. P25R0934458M year 2025?'"
)
args = argparser.parse_args()
user_query = (args.query,)

def main():
    response = PolicyAgent.get_api_response(query=user_query)
    print(response['output'])
                
#Invoking main function
if __name__ == '__main__':
    main()
