import os
from langchain_agent import LangChainAgent
import streamlit as st 

os.system('cls' if os.name == 'nt' else 'clear')

system_context = "Answer the Insurance Policy query using the API. Stamp References should be in full and be in uppercase. The API stores data from 2021 to 2025."
openapi_json_file = "openapi-policy.json"

def main():
    st.title("policy")
    st.set_page_config(page_title="policy Agent",
                       layout="centered")
    st.title("Let AI find answers for You 📖")
    st.header("Get Started...")
    
    user_query = st.text_input(label="What's your query?", value="Who is the client for stamp ref. P25R0934458M year 2025?")
    
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