import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Configure the API key
genai.configure(api_key=api_key)

# For text-only input, use the gemini-pro model
model = genai.GenerativeModel('gemini-1.5-flash')

print("Enter a text : ")
msg = input()

# Generate content
response = model.generate_content(msg)

print(response.text)
