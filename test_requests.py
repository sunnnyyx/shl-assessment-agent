from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

r = requests.get(url)

print(r.status_code)
print(r.text[:500])