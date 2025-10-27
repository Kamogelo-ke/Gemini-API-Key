from dotenv import load_dotenv
import os
from google import generativeai as genai
from utils import print_response

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("GEMINI_API_KEY not found. Add it to a .env file.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Write a short, friendly greeting.")
print_response(response)
