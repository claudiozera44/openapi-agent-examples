import os
from langchain_f1_agent import F1_Agent
import streamlit as st 

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    st.title("F1 OpenAPI Agent")
    st.set_page_config(page_title="F1 OpenAPI Agent",
                       layout="centered")
    st.title("Let AI find answers for You 📖")
    st.header("Get Started...")
    
    query = st.text_input(label="What's your query?", value="Who won in Monaco in 2024?")
    
    submit_button = st.button("Submit")
    if query:
        if submit_button:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            with st.spinner("Processing..."):
                response = F1_Agent.get_api_response(query=query)
                
                with st.expander("response"):
                    st.write(response['output'])
                
            st.success("Response has been provided!")

#Invoking main function
if __name__ == '__main__':
    main()  