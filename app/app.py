import os
import openai
from dotenv import find_dotenv, load_dotenv
import streamlit as st 

load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    st.set_page_config(page_title="Generate Children's Lullaby",
                       layout="centered")
    st.title("Let AI Write and Translate a Lullaby for You 📖")
    st.header("Get Started...")
    
    location_input = st.text_input(label="Where is the story set?", value="Zanzibar")
    main_character_input = st.text_input(label="What's the main charater's name", value="Maya")
    language_input = st.text_input(label="Translate the story into...", value="Italian")
    
    submit_button = st.button("Submit")
    if location_input and main_character_input and language_input:
        if submit_button:
                
            st.write("Submit button clicked")
            st.success("=== end of execution! ===")

 #Invoking main function
if __name__ == '__main__':
    main()  
