# Running the Haystack Agent Example

This guide will help you set up and run the Haystack Agent to query F1 race information.

## Prerequisites

- Python 3.7+
- OpenAI API key, which you can get by signing up at [OpenAI](https://platform.openai.com/)
- [FastAPI F1 Server](/f1-fastapi-server/README.md) running

## Setup Instructions

1. Set your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Start the FastAPI server following the instructions in the [README](/f1-fastapi-server/README.md)

4. Run the Haystack agent with your query:

    ```bash
    python haystack_agent.py "Who won the Monaco Grand Prix in 2024?"
    ```

## Note

Make sure the FastAPI server is running before executing queries with the Haystack agent.
