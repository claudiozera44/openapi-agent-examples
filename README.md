<div align="center">
 <a href="https://www.speakeasy.com/" target="_blank">
  <img width="1500" height="500" alt="Speakeasy" src="https://github.com/user-attachments/assets/0e56055b-02a3-4476-9130-4be299e5a39c" />
 </a>
 <br />
 <br />
  <div>
   <a href="https://speakeasy.com/docs/create-client-sdks/" target="_blank"><b>Docs Quickstart</b></a>&nbsp;&nbsp;//&nbsp;&nbsp;<a href="https://go.speakeasy.com/slack" target="_blank"><b>Join us on Slack</b></a>
  </div>
 <br />

</div>
<h1>
 OpenAPI agent examples
</h1>


</div>



This repository demonstrates how to build OpenAPI-powered AI agents using two popular frameworks, [LangChain](https://python.langchain.com/docs/introduction/) and [Haystack](https://haystack.deepset.ai/). These agents can process user queries, interact with APIs described by OpenAPI documents, and generate intelligent responses.

For an in-depth comparison of LangChain and Haystack, see [this article](https://www.speakeasy.com/openapi).

## Repository structure

The repository is organized into the following directories:

### 1. `f1-fastapi-server`

A mock Formula One (F1) API server built using FastAPI. This API serves as the backend for the agents.

- **Files:**
  - `main.py`: FastAPI application defining endpoints for querying F1 race winners.
  - `openapi.yaml`: OpenAPI specification describing the API's endpoints, request parameters, and response formats.
  - `README.md`: Instructions for setting up and running the F1 API server.
  - `requirements.txt`: Dependencies required to run the server.

### 2. `langchain-agent`

An AI agent built with LangChain that interacts with the F1 API to fetch race data based on user queries.

- **Files:**
  - `langchain_agent.py`: Script defining the LangChain agent.
  - `openapi.json`: OpenAPI document (converted to JSON format) for the F1 API.
  - `README.md`: Instructions for setting up and running the LangChain agent.
  - `requirements.txt`: Dependencies required for the LangChain agent.

### 3. `haystack-agent`

An AI agent built with Haystack that performs similar tasks as the LangChain agent.

- **Files:**
  - `haystack_agent.py`: Script defining the Haystack agent.
  - `openapi.yaml`: OpenAPI document for the F1 API.
  - `README.md`: Instructions for setting up and running the Haystack agent.
  - `requirements.txt`: Dependencies required for the Haystack agent.

## Setup instructions

### Prerequisites

- Python 3.9+
- A valid API key from [OpenAI](https://platform.openai.com/) or [Anthropic](https://anthropic.com/).

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ritza-co/openapi-agent-examples.git
   cd openapi-agent-examples
   ```

2. **Set up the F1 API server:**
   - Navigate to the `f1-fastapi-server` directory:

     ```bash
     cd f1-fastapi-server
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Run the server:

     ```bash
     uvicorn main:app --reload
     ```

   The server will be available at `http://127.0.0.1:8000`.

   To get the OpenAPI document for the API server, navigate to `http://127.0.0.1:8000/openapi.json`.

3. **Run the LangChain agent:**
   - Navigate to the `langchain-agent` directory:

     ```bash
     cd langchain-agent
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Set your Anthropic API key as an environment variable:

     ```bash
     export ANTHROPIC_API_KEY="your_api_key"
     ```

   - Run the agent with a query:

     ```bash
     python langchain_agent.py "Who won the Monaco Grand Prix in 2024?"
     ```

4. **Run the Haystack agent:**
   - Navigate to the `haystack-agent` directory:

     ```bash
     cd haystack-agent
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Set your OpenAI API key as an environment variable:

     ```bash
     export OPENAI_API_KEY="your_api_key"
     ```

   - Run the agent with a query:

     ```bash
     python haystack_agent.py "Who won the Monaco Grand Prix in 2024?"
     ```

## Comparison of LangChain and Haystack

Both LangChain and Haystack are capable frameworks for building OpenAPI-powered AI agents. See [this article](https://www.speakeasy.com/openapi) for an in-depth comparison.
