[![GitHub](https://img.shields.io/badge/GitHub-Repo-blue?logo=github&logoColor=white)](https://github.com/sncarenyang/llm-chatbot-ui)
[![Hugging Face Spaces](https://img.shields.io/badge/Hugging%20Face-Spaces-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAP5JREFUOE+lk7FqAkEURY+ltunEg0XX2sZGIbXfEPdLlnxJyDdYB62sbbUKpLbVNhyYFzbrrA74YJlh9r079973psed0cvUD4A+4HoCjsA85X0D/v/RBLBgBDxnQPfAEJgBY+A9gALA4tcbamSzS4xq4FOQAJgCDwV2CPKV8tZAJcAjMMkUe1vX+U+SMhfAJEHasQIWmXNN3abzDwHUrgcRGmYcgKe0bxrblHEB4E/pndMazNpSZGcsZdBlYJcEL9Afo75molJ2FxmPgmgPqlWNLGfwZGG6UiyEvLzHYDmoPkDDiNm9JR9uboiONcBXrpY1qmgs21x1QwyZcpvxt9NS09PlsPAAAAAElFTkSuQmCC&logoWidth=14)](https://huggingface.co/spaces/SNCarenYang/llm-chatbot-ui)
[![Gradio](https://img.shields.io/badge/Gradio-UI-yellow?logo=gradio)](https://gradio.app)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org)
[![GitHub stars](https://img.shields.io/github/stars/sncarenyang/llm-chatbot-ui?style=social)](https://github.com/sncarenyang/llm-chatbot-ui)
[![GitHub license](https://img.shields.io/github/license/sncarenyang/llm-chatbot-ui)](LICENSE)


# 🤖 LLM Chatbot UI (Multi-Model)

An interactive AI chatbot with ChatGPT-style UI, conversation memory, and multi-model support (Gemini / OpenAI).
Deployed on Hugging Face Spaces for real-time user interaction.

_______

## 🌐 Live Demo

👉 https://huggingface.co/spaces/SNCarenYang/llm-chatbot-ui

_______

## 🚀 Features
 - 💬 ChatGPT-style conversation UI (chat bubbles)
 - 🧠 Conversation memory (context-aware responses)
 - 🔀 Model selection (Gemini / OpenAI)
 - ⚡ Real-time interaction with loading feedback
 - ⚠️ Graceful error handling (quota, API issues)
 - 🌐 Deployed on Hugging Face Spaces


 
## 🧩 System Design
 ```text
User Input (Gradio UI)
        ↓
LLM Router (model selection)
        ↓
Gemini API / OpenAI API
        ↓
Response
        ↓
Chat UI + Memory update
```

## Tech Stack
- Python
- Gradio
- Gemini API
- OpenAI API
- Hugging Face Spaces


## 🏗️ Project Structure
```text
llm-chatbot-ui/
├── README.md
├── requirements.txt
├── app.py
└── app/
│    ├── llm_router.py
│    ├── gemini_client.py
│    └── openai_client.py
├── .gitignore
└── LICENSE
```


## ⚙ Installation (Local)
```bash
pip install -r requirements.txt
```
#### Set API Key:
```bash
export GOOGLE_API_KEY=your_api_key
# optional
export OPENAI_API_KEY=your_api_key
```
#### Run:
```bash
python app.py
```


##  ☁️ Deployment (Hugging Face Spaces)
 #### 1. Create a new Space (SDK: Gradio)
 #### 2. Upload:
 - app.py
 - requirements.txt
 - app/ folder
 #### 3. Add secrets:
 - **GOOGLE_API_KEY**
 - (optional) OPENAI_API_KEY
 #### 4. Wait for build



## 💡 Design Decisions
 - Gemini as default model
 - Free-tier access
 - Fast response time
 - Modular LLM router
 - Easy to extend to more models
 - Conversation memory
 - Improves contextual understanding
 - Gradio UI
 - Rapid prototyping and deployment



## ⚠️ Known Limitations
- Free-tier quota may be exceeded (Gemini)
- No persistent memory (session-based only)
- No streaming response (future improvement)



## 📈 Future Improvements
- Streaming responses (typing effect)
- Persistent memory (database / vector store)
- RAG integration (external knowledge)
- User authentication
- Chat history export



## 🧠 What This Project Demonstrates
- LLM API integration (Gemini / OpenAI)
- Multi-model system design
- Interactive UI development (Gradio)
- Conversation state management
- Cloud deployment (Hugging Face Spaces)
- Error handling & UX design



## 👩‍💻 Author

Caren Yang
AI Engineer | LLM / RAG / Applied AI



## ⭐ If you find this project interesting, feel free to star the repo!

## 📊 Repository Statistics

[![Linux SysAdmin Stats](https://github-readme-stats.vercel.app/api?username=sncarenyang&repo=llm-chatbot-ui&show_icons=true&theme=radical)](https://github.com/sncarenyang/llm-chatbot-ui)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=sncarenyang&layout=compact&theme=radical)](https://github.com/sncarenyang/llm-chatbot-ui)



> This project is built with Python, Gradio, Gemini and OpenAI APIs, and deployed on Hugging Face Spaces.

