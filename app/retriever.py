from langchain_chroma import Chroma
from app.embeddings import embeddings


db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)


def retrieve_assessments(query: str, k: int = 10):
    """
    Retrieve the top-k most relevant SHL assessments.
    """

    results = db.similarity_search(query, k=k)

    assessments = []

    for doc in results:
        assessments.append({
            "name": doc.metadata.get("name"),
            "url": doc.metadata.get("url"),
            "content": doc.page_content
        })

    return assessments