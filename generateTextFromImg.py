import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
organ = PIL.Image.open("./image/cookies.jpeg")
response = model.generate_content(["Tell me about this instrument", organ])
print(response.text)