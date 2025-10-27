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

# Create the model (use supported name)
model = genai.GenerativeModel("gemini-2.5-pro")

# Ask the user for input
prompt = input("Enter your prompt for Gemini: ")

# Generate content
response = model.generate_content(prompt)

# Print the model's response
print_response(response)
