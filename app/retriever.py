from langchain_chroma import Chroma
from app.embeddings import get_embeddings

_db = None

def get_db():
    global _db

    if _db is None:
        _db = Chroma(
            persist_directory="chroma_db",
            embedding_function=get_embeddings()
        )

    return _db


def retrieve_assessments(query: str, k: int = 10):
    db = get_db()

    results = db.similarity_search(query, k=k)

    assessments = []

    for doc in results:
        assessments.append({
            "name": doc.metadata.get("name"),
            "url": doc.metadata.get("url"),
            "content": doc.page_content
        })

    return assessments