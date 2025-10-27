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
model = genai.GenerativeModel("gemini-2.5-pro")

# Conversation history
conversation_history = []

print("Welcome to Gemini Chat! Type 'exit' to quit.\n")

while True:
    prompt = input("You: ")
    
    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    # Add user's message to the conversation history
    conversation_history.append({"role": "user", "content": prompt})
    
    # Combine history into a single string to provide context
    full_prompt = ""
    for msg in conversation_history:
        role = "User" if msg["role"] == "user" else "Gemini"
        full_prompt += f"{role}: {msg['content']}\n"
    
    # Generate Gemini response
    response = model.generate_content(full_prompt)
    
    # Print and store Gemini's response
    print_response(response)
    conversation_history.append({"role": "gemini", "content": response.text})
