# 📚 Book Summary AI

An AI-powered web application built using **FastAPI** that generates book summaries based on the user's selected summary length.

This project demonstrates backend web development using Python, FastAPI, Jinja2 templates, and Bootstrap.

---

## 🚀 Features

- 📖 Search for any book by name
- 📝 Choose summary length:
  - Short
  - Medium
  - Detailed
- 🎨 Clean Bootstrap user interface
- ⚡ FastAPI backend
- 🖥️ Dynamic HTML pages using Jinja2
- 🏗️ Service-based project architecture

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- Jinja2 Templates
- Bootstrap 5
- HTML5
- CSS
- Uvicorn

---

## 📂 Project Structure

```
book-summary-ai/

│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── services/
│      ai_service.py
│
├── templates/
│      index.html
│      result.html
│
├── static/
│
└── database/
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shashankreddy92/book-summary-ai.git
```

Move into the project directory

```bash
cd book-summary-ai
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

---

## 📷 Screenshots

### Home Page

[[HomePage](url)]()

### Summary Page

(Add screenshot here)

---

## 📌 How It Works

1. User enters a book name.
2. User selects the summary length.
3. FastAPI receives the request.
4. The backend calls the AI service.
5. The generated summary is displayed on the results page.

---

## 🔮 Future Enhancements

- 🤖 Integrate OpenAI or Gemini API
- 📚 Google Books API integration
- 🖼️ Display book cover images
- ⭐ Show ratings and reviews
- 💾 Store search history using SQLite
- 📄 Export summaries as PDF
- ❤️ Save favorite books
- 🔍 Search previous summaries

---

## 📖 Learning Outcomes

This project helped me learn:

- FastAPI fundamentals
- Routing
- HTML Forms
- Jinja2 Templates
- Service Layer Architecture
- Bootstrap UI
- Git & GitHub
- Python project structure

---

## 👨‍💻 Author

**Shashank Reddy**

GitHub: https://github.com/shashankreddy92

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
