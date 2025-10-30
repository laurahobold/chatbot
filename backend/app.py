import os
from openai import OpenAI, OpenAIError

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_model(prompt):
    try:
        resp = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            stream=False
        )
        return resp.choices[0].message.content
    except OpenAIError as e:
        print("OpenAI error:", e)
        return "Tente novamente mais tarde."
