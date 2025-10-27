# main.py
from dotenv import load_dotenv
import os
from google import generativeai as genai
from utils import print_response

# Load environment variables
load_dotenv()

# Get the API key
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("Error: GEMINI_API_KEY not found. Add it to your .env file.")

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Create the model
model = genai.GenerativeModel("gemini-pro")

# Generate content
response = model.generate_content("Write a short, friendly greeting about coding in Python.")

# Print the model's response
print_response(response)
