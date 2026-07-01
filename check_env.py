from dotenv import load_dotenv
import os

load_dotenv()

print(os.getcwd())
print(os.getenv("GOOGLE_API_KEY"))