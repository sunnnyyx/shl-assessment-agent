from fastapi import FastAPI

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "SHL Assessment Recommender API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }