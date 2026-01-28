
# Build a RAG API with FastAPI

**Project Link:** [View Project](http://learn.nextwork.org/projects/ai-devops-api)

**Author:** Krithika Jain  

---

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_g3h4i5j6)

---

## Introducing Today's Project!

In this project, I will demonstrate how I implement RAG API using FastAPI. I'm doing this project to learn Retrieval Augmented Generation, how it works using python and use Olama LLM and ChromaDB for the entire implementation end to end. 

### Key services and concepts

Services I used were FastAPI, chromadb, ollama, uvicorn server and swaggerUI. Key concepts I learnt include setting up the environment and model locally, creating knowledge base and embeddings, creating API's to retrieve and add to chromadb followed by generation.

### Challenges and wins

This project took me approximately an hour and a half to complete. The most challenging part was my server wasn't running due to multiple other processes running. It was most rewarding to build and see all the endpoints working and generating the output.

### Why I did this project

I did this project because I needed to refresh my RAG concepts practically.

---

## Setting Up Python and Ollama

In this step, I'm setting up Python and Ollama. Python is programming language which I will use to write API code and Ollama is an open source LLM (Large Language Model) which runs locally. 

### Python and Ollama setup

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_i9j0k1l2)

### Verifying Python is working

### Ollama and tinyllama ready

Ollama is an open-source LLM to run models on your machine and here I downloaded the tinyllama model because it's an SLM (small language model) with 1.1 billion parameters which is just enough to to understand and generate text. The model will help my RAG API by acting as a brain behind the RAG API responses.

---

## Setting Up a Python Workspace

In this step, I'm setting up a project folder containing the python code, config files and data. This will keep things organized and easier to manage.

### Python workspace setup

### Virtual environment

A virtual environment is an isolated python environment that keeps the python and other dependencies from other projects in the computer. I created one for this project to prevent any conflicts and such that it can have it's own set of packages and version.
To create a virtual environment, I run the command python3 -m venv venv and once the folder is created we need to activate it using the command source venv/bin/activate.

### Dependencies

The packages I installed are: FastAPI is used for building API's quickly, Chroma is a vector database used for storing document embeddings, Uvicorn is a server that runs our app on the machine where it listens for incoming requests on the machine and routes them to right functions in the code and finally, Ollama here is a python client library that let's the code talk to models like in our case tinyllama.

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_u1v2w3x4)

---

## Setting Up a Knowledge Base

In this step, I'm creating a knowledge base it is a going to provide the model with up-to-date information about specific topics becasue the models are either trained on vast dataset or limited training data. I need it here because this will act as a Retrieval part of RAG to retrive relevant information before generating that answer.
After this we will create a script that prepares the content and make it searchable.

### Knowledge base setup

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_t1u2v3w4)

### Embeddings created

Embeddings are numerical representation of text that capture meaning. Words with similar meanings are placed close together, while unrelated words are far apart. 
I created them by writing a script that imports the chromadb library. 
The db/ folder contains subfolders with long UUID-like name which has the raw embedding vectors and associated data, it also contains chroma.sqlite3 which stores references and metadata about the document and embeddings. This is important for RAG because it contains our knowledge bases's embeddings so that chroma can search through them when our API is running.

---

## Building the RAG API

In this step, I'm building a RAG API. An API is a set of rules that allow different applications communicate and interact with each other. FastAPI is a modern python web framework for building APIs. I'm creating this because it is designed to be fast, easy, automatically generates interactive documentation and Big Tech compaines like Uber, Netflix use FastAPI for their API's.

### FastAPI setup

### How the RAG API works

My RAG API works by creating a webserver with one endpoint /query, let's see step by step:
1. question arrives to the api /query
2. search the docs which is the knowledge base we created where it finds the text matching the question.
3. get the most relevant information from the doc called as context here.
4. to generate the answer the question and the matching text are sent to tinyllama
5. sends back an answer.

So it Retrieve's relevant info, then augment the LLM's generation with that info.

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_f3g4h5i6)

---

## Testing the RAG API

In this step, I'm testing my RAG API. I'll test it using command line first then try Swagger UI, this automatically generates interactive documentation page for my FastAPI server. I'll use it to visually explore my API endpoints and see what parameters they accept.

### Testing the API

### API query breakdown

I queried my API by running the command  curl -X POST "http://127.0.0.1:8000/query" -G --data-urlencode "q=What is Kubernetes?"
The command uses the POST method, which is used to send data to the server or create or update a resource.
The API responded with an answer.

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_g3h4i5j6)

### Swagger UI exploration

Swagger UI is an automatically generated interactive page to test API endpoints. I used it to test POST /query endpoint by opening the browser and going to: http://127.0.0.1:8000/docs.
The best part about using Swagger UI was visually exploring the endpoints and see what parameters it takes and test them out all in the browezer without any cli commands.

---

## Adding Dynamic Content

In this project extension, I'm adding a new API endpoint that allows users to dynamically add the content to the knowledge base.

### Adding the /add endpoint

![Image](http://learn.nextwork.org/nostalgic_orange_optimistic_jellyfish/uploads/ai-devops-api_w9x0y1z2)

### Dynamic content endpoint working

The /add endpoint allows me to dynamically add documents/ texts to the knowlegde base we created earlier using chromadb. This is useful because in production systems, knowledge bases need to be updated frequently as new information becomes available. 

---

---
