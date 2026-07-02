import json

from langchain_core.documents import Document
from langchain_chroma import Chroma

from app.embeddings import get_embeddings


def build_vector_store():
    with open("data/assessments.json", "r") as f:
        assessments = json.load(f)

    documents = []

    for assessment in assessments:
        text = f"""
        Name: {assessment.get("title")}
        Description: {assessment.get("description")}
        Duration: {assessment.get("duration")}
        Remote Testing: {assessment.get("remote_testing")}
        Adaptive: {assessment.get("adaptive")}
        URL: {assessment.get("url")}
        """

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "name": assessment.get("title"),
                    "url": assessment.get("url")
                }
            )
        )

    Chroma.from_documents(
        documents=documents,
        embedding=get_embeddings(),
        persist_directory="chroma_db"
    )

    print(f"Stored {len(documents)} assessments.")