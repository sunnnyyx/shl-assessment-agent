from dotenv import load_dotenv
import os
from google import genai

# Load .env
load_dotenv()

# Create client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Generate a simple response
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)