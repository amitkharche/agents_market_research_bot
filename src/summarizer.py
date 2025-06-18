"""
Summarize text using OpenAI GPT.
"""

import os
from dotenv import load_dotenv
import openai

# ✅ Load API key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# ✅ Function to summarize input text
def summarize_text(text, max_tokens=150):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"""Summarize the following text:

{text}"""
            }
        ],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content
