import os
from google import genai


GEMINI_MODEL = "gemini-2.5-flash"


def ask_gemini(prompt: str) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        return "Error: GOOGLE_API_KEY is not set."

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )

    return response.text
