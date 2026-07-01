from app.retriever import retrieve_assessments

results = retrieve_assessments(
    "Java developer with 4 years experience"
)

for r in results:
    print("=" * 50)
    print(r)