import os
from groq import Groq
from prompts import PROMPT

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from Streamlit Secrets.")

client = Groq(api_key=api_key)


def analyze_resume(resume_text):

    prompt = PROMPT.format(resume=resume_text)

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
