import gradio as gr

from app.llm_router import ask_llm


def respond(message, history, provider):
    if not message.strip():
        return history, ""

    history = history or []

    reply = ask_llm(
        message=message,
        provider=provider,
        history=history,
    )

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})

    return history, ""


def clear_chat():
    return []


with gr.Blocks(title="LLM Chatbot UI") as demo:
    gr.Markdown(
        """
        # 🤖 LLM Chatbot UI (Multi-Model)

        Interactive AI chatbot with conversation memory.

        • Gemini (default)  
        • Optional OpenAI  
        • Model selection  
        • ChatGPT-style conversation UI  
        • Deployed on Hugging Face Spaces
        """
    )

    provider = gr.Radio(
        choices=["Gemini", "OpenAI"],
        value="Gemini",
        label="Choose model provider",
    )

    chatbot = gr.Chatbot(
        label="Chat",
        type="messages",
        height=500,
    )

    msg = gr.Textbox(
        label="Your message",
        placeholder="Ask anything, e.g. Explain RAG in simple terms.",
        lines=3,
    )

    with gr.Row():
        submit = gr.Button("Submit", variant="primary")
        clear = gr.Button("Clear chat")

    submit.click(respond, inputs=[msg, chatbot, provider], outputs=[chatbot, msg])
    msg.submit(respond, inputs=[msg, chatbot, provider], outputs=[chatbot, msg])
    clear.click(clear_chat, inputs=[], outputs=[chatbot])


if __name__ == "__main__":
    demo.launch()
