
# Build a RAG API with FastAPI

**Project Link:** [View Project](https://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/docs/ai-devops-api)

**Author:** Krithika Jain  

In this project, I will demonstrate how I implement RAG API using FastAPI. I'm doing this project to learn Retrieval Augmented Generation, how it works using python and use Olama LLM and ChromaDB for the entire implementation end to end. 

### Key services and concepts

Services I used were FastAPI, chromadb, ollama, uvicorn server and swaggerUI. Key concepts I learnt include setting up the environment and model locally, creating knowledge base and embeddings, creating API's to retrieve and add to chromadb followed by generation.

### FastAPI setup

### How the RAG API works

My RAG API works by creating a webserver with one endpoint /query, let's see step by step:
1. question arrives to the api /query
2. search the docs which is the knowledge base we created where it finds the text matching the question.
3. get the most relevant information from the doc called as context here.
4. to generate the answer the question and the matching text are sent to tinyllama
5. sends back an answer.

So it Retrieve's relevant info, then augment the LLM's generation with that info.


## Testing the RAG API

In this step, I'm testing my RAG API. I'll test it using command line first then try Swagger UI, this automatically generates interactive documentation page for my FastAPI server. I'll use it to visually explore my API endpoints and see what parameters they accept.

### Testing the API

### API query breakdown

I queried my API by running the command  curl -X POST "http://127.0.0.1:8000/query" -G --data-urlencode "q=What is Kubernetes?"
The command uses the POST method, which is used to send data to the server or create or update a resource.
The API responded with an answer.

### Swagger UI exploration

Swagger UI is an automatically generated interactive page to test API endpoints. I used it to test POST /query endpoint by opening the browser and going to: http://127.0.0.1:8000/docs.
The best part about using Swagger UI was visually exploring the endpoints and see what parameters it takes and test them out all in the browezer without any cli commands.

## Adding Dynamic Content

In this project extension, I'm adding a new API endpoint that allows users to dynamically add the content to the knowledge base.



