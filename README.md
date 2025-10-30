# Chatbot

Experimental chatbot using AgentOS and OpenAI.  
The long-term goal is to evolve it into a support / assistance bot.

---

## ✅ Current Status

- Backend running with **AgentOS** using **FastAPI + Uvicorn**
- Frontend with **AgentUI** fully connected to the backend
- Live connection to **OpenAI API** with active billing
- Local development environment fully working
- **Docker / Docker Compose** set up for future deployment
- **n8n** webhook workflow in progress for user data capture

Backend entrypoint (based on `agentos.py`):  
:contentReference[oaicite:0]{index=0}

There is also a simple OpenAI test script:  
:contentReference[oaicite:1]{index=1}

---

## 🚧 In Progress

- **User memory** is not fully functional yet  
  (bot responds correctly, but does not remember previous inputs)
- Testing a **SQLite profile** solution to store information like user name
- Integrating the profile into the chat f
