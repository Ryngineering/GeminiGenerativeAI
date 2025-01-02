import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def fetch_webpage_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    return text

def summarize_text(text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"Summarize the following text in less than 100 words : {text}")
    return response.text


url = "https://ai.google.dev/gemini-api/docs/models/generative-models"

fetch_webpage_text = fetch_webpage_text(url)
summary = summarize_text(fetch_webpage_text)

print(f"Summary \n {summary}")
