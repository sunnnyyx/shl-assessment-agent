from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = None

def get_embeddings():
    global _embeddings

    print("Step 1")

    if _embeddings is None:
        print("Step 2")

        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Step 3")

    print("Step 4")

    return _embeddings