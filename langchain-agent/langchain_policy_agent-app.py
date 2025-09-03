import os
from langchain_policy_agent import PolicyAgent
import streamlit as st 

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    st.title("policy")
    st.set_page_config(page_title="policy Agent",
                       layout="centered")
    st.title("Let AI find answers for You 📖")
    st.header("Get Started...")
    
    query = st.text_input(label="What's your query?", value="Who is the client for stamp ref. P25R0934458M year 2025?")
    
    submit_button = st.button("Submit")
    if query:
        if submit_button:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            with st.spinner("Processing..."):
                response = PolicyAgent.get_api_response(query=query)
                
                with st.expander("response"):
                    st.write(response['output'])
                
            st.success("Response has been provided!")

#Invoking main function
if __name__ == '__main__':
    main()  