# 🤖 AI Study Buddy

A beginner-friendly AI chatbot built using Google's Gemini API. This chatbot acts as a friendly programming tutor that explains concepts in simple language, provides examples, and stays in character using a custom system prompt.

## ✨ Features

- 📚 Friendly AI programming tutor
- 💡 Explains concepts in simple English
- 📝 Provides examples whenever possible
- 🎭 Uses a custom system prompt (persona)
- 🚫 Politely redirects off-topic questions
- ⚡ Powered by Google's Gemini API

## 🛠️ Technologies Used

- Python 3
- Google Gemini API
- python-dotenv

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/AI-Study-Buddy.git
```

2. Navigate to the project folder:

```bash
cd AI-Study-Buddy
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## 🔑 Configure API Key

Create a file named `.env` in the project directory and add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your own Gemini API key.

> **Note:** Never upload your `.env` file or API key to GitHub.

## ▶️ Run the Chatbot

```bash
python chatbot.py
```

## 💬 Example Questions

- What is Python?
- Explain loops like I'm 10 years old.
- What are variables?
- Write a function to add two numbers.
- Who will win the FIFA World Cup?

## 📁 Project Structure

```
AI-Study-Buddy/
│── chatbot.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env (not uploaded)
```

## 📜 License

This project is created for educational and learning purposes.