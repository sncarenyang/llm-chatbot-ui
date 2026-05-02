from app.gemini_client import ask_gemini
from app.openai_client import ask_openai


def format_history(history):
    if not history:
        return ""

    lines = []
    for item in history[-10:]:
        role = item.get("role", "")
        content = item.get("content", "")
        if role == "user":
            lines.append(f"User: {content}")
        elif role == "assistant":
            lines.append(f"Assistant: {content}")

    return "\n".join(lines)


def ask_llm(message: str, provider: str, history=None) -> str:
    provider = provider.lower()
    context = format_history(history)

    if context:
        prompt = f"""
You are a helpful AI assistant.

Conversation so far:
{context}

Current user message:
{message}

Please answer the current user message while considering the conversation history.
"""
    else:
        prompt = message

    try:
        if provider == "gemini":
            return ask_gemini(prompt)

        if provider == "openai":
            return ask_openai(message=message, history=history)

        return f"Unsupported provider: {provider}"

    except Exception as error:
        return f"Error: {error}"
