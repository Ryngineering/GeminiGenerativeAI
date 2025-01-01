import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure the API key
genai.configure(api_key=api_key)

# For text-only input, use the gemini-pro model
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate content
response = model.generate_content("Write a short story about a cat who goes on an adventure.")

print(response.text)
