<div align="center">
 <a href="https://windlead.co.uk/" target="_blank">
  <img width="auto" height="500" alt="windlead" src="https://windlead.co.uk/wp-content/uploads/2025/06/WIND-LEAD-2.png" />
 </a>
 <br />
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
  - `langchain-agent.py`: Script defining the LangChain agent.
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

### 4. `policy-fastapi-server`

A mock Policy (Insurance, London Market) API server built using FastAPI. This API serves as the backend for the agents.

- **Files:**
  - `main.py`: FastAPI application defining endpoints for querying London Market policies.
  - `openapi.yaml`: OpenAPI specification describing the API's endpoints, request parameters, and response formats.
  - `README.md`: Instructions for setting up and running the Policy API server.
  - `requirements.txt`: Dependencies required to run the server.

## Setup instructions

### Prerequisites

- Python 3.9+
- A valid API key from [OpenAI](https://platform.openai.com/) or [Anthropic](https://anthropic.com/).

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/claudiozera44/openapi-agent-examples.git
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

3. **Set up the Policy API server:**
   - Navigate to the `policy-fastapi-server` directory:

     ```bash
     cd policy-fastapi-server
     ```

   - Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

   - Run the server:

     ```bash
     uvicorn main:app --reload --port 7000
     ```

   The server will be available at `http://127.0.0.1:7000`.

   To get the OpenAPI document for the API server, navigate to `http://127.0.0.1:7000/openapi.json`.

4. **Run the LangChain agent:**
   - Navigate to the `langchain-agent` directory:

     ```bash
     cd langchain-agent
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
     python langchain_f1_agent-console.py "Who won the Monaco Grand Prix in 2024?"
     python langchain_policy_agent-console.py "Who is the client for stamp ref. P25R0934458M year 2025?"
     ```

5. **Run the streamlit app**

     ```
     streamlit run langchain-agent-f1-app.py
     streamlit run langchain-agent-policy-app.py
     ```

6. **(OPTIONAL) Run the Haystack agent:**
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

## Credits

Credits to [Chai Landau](https://github.com/chailandau), as this repository was initially forked from repo [speakeasy-api/openapi-agent-examples](https://github.com/speakeasy-api/openapi-agent-examples)

