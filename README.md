# SHL Assessment Recommendation System

An AI-powered Retrieval-Augmented Generation (RAG) application that helps recruiters discover the most suitable SHL assessments based on hiring requirements and answer questions about SHL's assessment catalog.

Built using FastAPI, ChromaDB, LangChain, HuggingFace Embeddings, and DeepSeek (via OpenRouter).

---

## Features

- AI-powered assessment recommendations
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Multi-turn conversation support
- Assessment comparison
- Assessment information lookup
- Automatic conversation intent detection
- Prompt injection protection
- Structured recommendation output
- REST API with Swagger documentation

---

## Project Architecture

```
                User Query
                     │
                     ▼
             FastAPI (/chat)
                     │
                     ▼
         Intent Detection Layer
                     │
                     ▼
      Chroma Vector Database Search
                     │
                     ▼
     Top-K Relevant SHL Assessments
                     │
                     ▼
      DeepSeek Chat Model (OpenRouter)
                     │
                     ▼
      JSON Recommendation Extraction
                     │
                     ▼
          Structured API Response
```

---

# Tech Stack

### Backend

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic

### AI / RAG

- LangChain
- ChromaDB
- HuggingFace Embeddings
- sentence-transformers/all-MiniLM-L6-v2
- DeepSeek Chat V3
- OpenRouter API

### Data Processing

- JSON
- Regular Expressions

---

# Folder Structure

```
.
├── app
│   ├── agent.py
│   ├── config.py
│   ├── embeddings.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── main.py
│
├── chroma_db/
│
├── data/
│   └── assessments.json
│
├── build_db.py
│
├── requirements.txt
│
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/shl-assessment-recommender.git

cd shl-assessment-recommender
```

Create a virtual environment

Mac/Linux

```bash
python3 -m venv venv
```

Windows

```bash
python -m venv venv
```

Activate it

Mac/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

# Build the Vector Database

The assessment dataset is converted into vector embeddings using HuggingFace's MiniLM model and stored inside ChromaDB.

Run

```bash
python build_db.py
```

Expected output

```
Stored XX assessments.
```

---

# Running the Server

```bash
uvicorn app.main:app --reload
```

Server

```
http://127.0.0.1:8000
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

GET

```
/health
```

Response

```json
{
    "status":"ok"
}
```

---

## Chat Endpoint

POST

```
/chat
```

Request

```json
{
  "messages":[
    {
      "role":"user",
      "content":"Recommend an assessment for a software engineer."
    }
  ]
}
```

Example Response

```json
{
  "reply":"For a software engineer, I recommend SHL Coding Skills Assessment and Simulations...",
  "recommendations":[
    {
      "name":"SHL Coding Skills Assessment and Simulations",
      "url":"https://www.shl.com/..."
    }
  ],
  "conversation_type":"recommendation",
  "end_of_conversation":false
}
```

---

# Supported Conversation Types

The system automatically detects user intent.

### Recommendation

Example

```
Recommend an assessment for a software engineer.
```

---

### Information

Example

```
Tell me about OPQ.
```

---

### Comparison

Example

```
Compare OPQ and Verify.
```

---

### Clarification

Example

```
I need an assessment.
```

If insufficient information is provided, the assistant asks a clarification question before recommending assessments.

---

### Goodbye

Example

```
Thank you.
```

The assistant politely ends the conversation.

---

# Retrieval Pipeline

1. User submits a query.
2. Intent detection categorizes the request.
3. Query is embedded using MiniLM.
4. ChromaDB retrieves the most relevant assessments.
5. Retrieved assessments are injected into the LLM prompt.
6. DeepSeek generates the final answer.
7. Recommended assessment names are extracted from structured JSON.
8. Matching assessment URLs are returned.

---

# Prompt Safety

The assistant follows strict system instructions.

It:

- only recommends retrieved assessments
- never hallucinates assessment names
- ignores prompt injection attempts
- never invents assessment capabilities
- asks clarification questions when needed

---

# Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```

Used for semantic similarity search over SHL assessment descriptions.

---

# Vector Database

ChromaDB stores:

- assessment title
- description
- duration
- adaptive flag
- remote testing support
- URL

Metadata stored:

```
name
url
```

---

# AI Model

```
deepseek/deepseek-chat-v3
```

Accessed through OpenRouter.

---

# Sample Queries

```
Recommend an assessment for hiring software engineers.
```

```
Recommend an assessment for graduates.
```

```
Tell me about OPQ.
```

```
Compare OPQ and Verify.
```

```
Recommend a coding assessment.
```

```
Which assessment evaluates Java skills?
```

```
I need an assessment.
```

---

# Design Decisions

## Why RAG?

Instead of fine-tuning a model on SHL data, Retrieval-Augmented Generation ensures:

- responses are grounded in the latest assessment data
- lower hallucination rate
- smaller infrastructure requirements
- easier dataset updates

---

## Why ChromaDB?

- lightweight
- local vector storage
- LangChain integration
- ideal for small-to-medium retrieval tasks

---

## Why MiniLM?

- lightweight
- fast inference
- strong semantic retrieval performance
- open source

---

## Why FastAPI?

- automatic Swagger documentation
- high performance
- simple deployment
- clean API structure

---

# Known Limitation

The SHL product catalog visually displays assessment type indicators (e.g., A, P, K), but these values were not reliably available through the publicly accessible HTML or API responses during data extraction. As a result, the current implementation does not include a `test_type` field in the indexed dataset.

All other required assessment metadata is successfully retrieved and used by the recommendation engine.

---

# Future Improvements

- Add frontend interface (React / Next.js)
- Conversation memory with LangGraph
- Streaming responses
- Authentication
- Docker deployment
- Redis caching
- Better reranking
- Hybrid search (BM25 + embeddings)
- Automatic dataset updates
- Test type support if SHL exposes structured metadata

---

# Author

**Sunny Chaudhary**

GitHub

```
https://github.com/sunnnyyx
```

LinkedIn

```
https://linkedin.com/in/sunny-chaudhary
```

---

# License

This project was developed as part of the SHL AI Engineering Internship Assignment and is intended for educational and evaluation purposes.