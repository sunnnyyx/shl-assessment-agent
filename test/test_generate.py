from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

body = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Say hello."
                }
            ]
        }
    ]
}

response = requests.post(url, json=body)

print(response.status_code)
print(response.text)