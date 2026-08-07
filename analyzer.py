import os
from groq import Groq
from prompts import PROMPT

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def analyze_resume(resume_text):

    prompt = PROMPT.format(resume=resume_text)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

    
    