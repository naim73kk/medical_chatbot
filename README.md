# 🩺 Medical Chatbot (RAG-based AI Assistant)

An AI-powered **medical chatbot** built using **Retrieval-Augmented Generation (RAG)** to provide accurate, context-aware answers based on medical documents.

⚠️ **Disclaimer**: This project is for **educational and research purposes only**. It does **not** provide medical diagnosis or replace professional medical advice.

---

## 📌 Project Overview

The **Medical Chatbot** is designed to answer medical-related questions using **domain-specific knowledge** rather than relying only on a general language model.

By combining document retrieval with a large language model, the chatbot produces responses that are:
- More reliable  
- Context-aware  
- Less prone to hallucinations  

---

## 🧠 Architecture (RAG)

The system follows a **Retrieval-Augmented Generation** pipeline:

1. User submits a medical question  
2. Relevant medical documents are retrieved  
3. Retrieved context is injected into the prompt  
4. The language model generates a grounded response  
5. The answer is returned to the user  

---

## 🗂️ Repository Structure

```text
medical_chatbot/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── data/                  # Medical documents
│
├── src/                   # Core logic
│   ├── chatbot.py         # LLM interaction logic
│   ├── retriever.py       # Document retrieval
│   └── embeddings.py      # Embedding creation
│
├── templates/             # HTML templates
│   └── index.html
│
├── static/                # CSS, JS, assets
│
└── research/              # Experiments and notes
```

---

## ⚙️ Technologies Used

- **Python 3.10+**
- **Flask** – backend web framework
- **OpenAI API** – large language model
- **Embeddings & Vector Search**
- **Retrieval-Augmented Generation (RAG)**
- **Conda** – environment management
- **HTML / CSS (Jinja2)** – frontend templating

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/naim73kk/medical_chatbot.git
cd medical_chatbot
```

### 2️⃣ Create and activate Conda environment
```bash
conda create -n medibot python=3.10
conda activate medibot
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 OpenAI API Configuration

### Set API key (Windows – PowerShell)
```powershell
setx OPENAI_API_KEY "sk-xxxxxxxxxxxxxxxx"
```

Restart PowerShell after setting the key.

Verify:
```powershell
echo $env:OPENAI_API_KEY
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser at:
```
http://127.0.0.1:5000
```

---

## ✨ Features

- Medical question answering
- Context-aware responses using RAG
- Reduced hallucinations
- Simple web interface
- Modular and extensible codebase

---

## ⚠️ Disclaimer

This chatbot is an **academic project only** and must **not** be used for real medical decision-making.
