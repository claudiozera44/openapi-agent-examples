import os
import argparse
from langchain_f1_agent import F1_Agent

os.system('cls' if os.name == 'nt' else 'clear')

argparser = argparse.ArgumentParser()
argparser.add_argument(
    "query", type=str, help="User query. E.g: 'Who won in Monaco in 2024?'"
)
args = argparser.parse_args()
user_query = (args.query,)

def main():
    response = F1_Agent.get_api_response(query=user_query)
    print(response['output'])
                
#Invoking main function
if __name__ == '__main__':
    main()
