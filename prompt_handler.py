from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_response(user_prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content
