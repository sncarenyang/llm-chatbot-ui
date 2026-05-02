import os
from openai import OpenAI


OPENAI_MODEL = "gpt-4o-mini"


def ask_openai(message: str, history=None) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "Error: OPENAI_API_KEY is not set."

    client = OpenAI(api_key=api_key)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Keep answers clear and practical.",
        }
    ]

    if history:
        for item in history[-10:]:
            role = item.get("role")
            content = item.get("content")
            if role in {"user", "assistant"} and content:
                messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=0.4,
    )

    return response.choices[0].message.content
