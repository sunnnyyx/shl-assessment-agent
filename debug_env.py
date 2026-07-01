from dotenv import load_dotenv
import os

load_dotenv()

for key in [
    "GOOGLE_API_KEY",
    "GOOGLE_GENAI_USE_VERTEXAI",
    "GOOGLE_CLOUD_PROJECT",
    "GOOGLE_CLOUD_LOCATION",
    "GOOGLE_APPLICATION_CREDENTIALS",
]:
    print(f"{key} =", os.getenv(key))