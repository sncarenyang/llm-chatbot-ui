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



 

 
