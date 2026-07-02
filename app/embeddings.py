from langchain_openai import OpenAIEmbeddings
from app.config import OPENROUTER_API_KEY

_embeddings = None

def get_embeddings():
    global _embeddings

    if _embeddings is None:
        print("Loading OpenRouter embeddings...", flush=True)

        _embeddings = OpenAIEmbeddings(
            model="openai/text-embedding-3-small",
            openai_api_key=OPENROUTER_API_KEY,
            openai_api_base="https://openrouter.ai/api/v1",
        )

        print("Embeddings ready!", flush=True)

    return _embeddings