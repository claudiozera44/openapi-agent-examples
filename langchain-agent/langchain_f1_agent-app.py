import os
from langchain_agent import LangChainAgent
import streamlit as st 

os.system('cls' if os.name == 'nt' else 'clear')

system_context = "Answer the F1 query using the API. Race names with two words should be separated by an underscore and be in lowercase. The API stores data from 2021 to 2024."
openapi_json_file = "openapi-f1.json"

def main():
    st.title("F1 OpenAPI Agent")
    st.set_page_config(page_title="F1 OpenAPI Agent",
                       layout="centered")
    st.title("Let AI find answers for You 📖")
    st.header("Get Started...")
    
    user_query = st.text_input(label="What's your query?", value="Who won in Monaco in 2024?")
    
    submit_button = st.button("Submit")
    if user_query:
        if submit_button:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            with st.spinner("Processing..."):
                response = LangChainAgent.get_api_response(query=user_query, 
                                                        openapi_json_file=openapi_json_file,
                                                        system_context=system_context)  
                
                with st.expander("response"):
                    st.write(response['output'])
                
            st.success("Response has been provided!")

#Invoking main function
if __name__ == '__main__':
    main()  