# Running the Policy API Server

To run the Policy API server, follow these steps:

1. Install the required dependencies using `pip install -r requirements.txt`.

2. Run the FastAPI server using `uvicorn main:app --reload --port 7000`.

3. The API server will start on `http://127.0.0.1:7000/` by default.

## Getting the OpenAPI Spec

To get the OpenAPI spec for the API server, navigate to `http://127.0.0.1:7000/openapi.json`and save the JSON response to a file.
