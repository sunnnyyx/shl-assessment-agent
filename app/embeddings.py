from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = None

def get_embeddings():
    global _embeddings

    if _embeddings is None:
        print("Loading HuggingFace embeddings...", flush=True)

        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Embeddings loaded!", flush=True)

    return _embeddings