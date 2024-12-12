# Running the LangChain Agent Example

This guide will help you set up and run the LangChain Agent to query F1 race information using Anthropic's Claude model.

## Prerequisites

- Python 3.7+
- Anthropic API key
- [FastAPI F1 Server](https://github.com/AbdulDavids/example-fast-api-f1)

## Setup Instructions

1. Set your Anthropic API key as an environment variable:

    ```bash
    export ANTHROPIC_API_KEY='your-api-key-here'
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the FastAPI server following the instructions in the [README](/f1-fastapi-server/README.md)

4. Run the LangChain agent with your query:

    ```bash
    python langchain_agent.py "Who won the Monaco Grand Prix in 2024?"
    ```

## Note

Make sure the FastAPI server is running before executing queries with the LangChain agent.
