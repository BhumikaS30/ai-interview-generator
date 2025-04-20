# AI Interview Tools

This repository contains two powerful tools for leveraging OpenAI's GPT models to enhance technical interview preparation:

1. **AI Interview Question Generator**
2. **Mock Interview Simulator**

---

## 🔧 Technologies Used
- Python 3.8+
- Streamlit (for UI)
- OpenAI Python SDK
- dotenv (for managing API keys)

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-interview-tools.git
cd ai-interview-tools
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up OpenAI API Key
Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key
```

---

## 🚀 Running the Apps

### 💡 1. Interview Question Generator
Generates interview questions based on selected role, experience, and skills.

```bash
streamlit run interview_question_generator.py
```

### 🧠 2. Mock Interview Simulator
Interactive mock interview session with AI simulating an interviewer.

```bash
streamlit run mock_interview_simulator.py
```

---

## 📌 Features

### ✅ Interview Question Generator
- Role-based question generation
- Customize years of experience and skills
- Instant question display via OpenAI

### ✅ Mock Interview Simulator
- Role and experience setup
- Skills input (auto-parsing)
- Multi-turn interaction like a real interview
- Real-time responses and feedback
