# Running the LangChain Agent Example

This guide will help you set up and run the LangChain Agent to query policy information using OpenAI's gpt model.

## Prerequisites

- Python 3.7+
- OpenAI API key, which you can get by signing up at [OpenAI](https://openai.com/)
- [FastAPI Policy Server](/policy-fastapi-server/README.md) running

## Setup Instructions

1. Set your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the FastAPI server following the instructions in the [README](/policy-fastapi-server/README.md)

4. Run the LangChain agent with your query:

    ```bash
    python langchain_policy_agent-console.py "Who is the client for stamp ref. P25R0934458M year 2025?"
    ```

5. Run the streamlit app

     ```
     streamlit run langchain-agent-f1-app.py
     streamlit run langchain-agent-policy-app.py
     ```

## Note

Make sure the FastAPI server is running before executing queries with the LangChain agent.
