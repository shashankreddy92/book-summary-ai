# 📚 Book Summary AI

An AI-powered web application built with **FastAPI** that generates intelligent book summaries using **Google Gemini AI**, fetches book information from the **Google Books API**, and stores search history using **SQLite**.

---

# 🚀 Features

- 📖 Search any book by title
- 🤖 AI-generated summaries using Google Gemini
- 📏 Choose summary length
  - Short
  - Medium
  - Detailed
- 📕 Displays book cover
- ✍️ Shows author information
- 🏢 Displays publisher details
- 📅 Published date
- ⭐ Average rating
- 📄 Book description
- 💾 Stores search history in SQLite
- 🎨 Responsive Bootstrap UI
- ⚡ FastAPI backend
- 🧩 Modular service-based architecture

---

# 🛠️ Tech Stack

## Backend

- Python 3
- FastAPI
- Uvicorn

## AI

- Google Gemini API

## APIs

- Google Books API

## Frontend

- HTML5
- Bootstrap 5
- Jinja2 Templates

## Database

- SQLite

## Others

- Requests
- Python-dotenv
- Git
- GitHub

---

# 📂 Project Structure

```text
book-summary-ai/

├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── database/
│   └── books.db
│
├── services/
│   ├── ai_service.py
│   ├── book_service.py
│   └── database_service.py
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
│
├── screenshots/
│   ├── home.png
│   └── result.png
│
└── static/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shashankreddy92/book-summary-ai.git
```

Move into the project

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

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_BOOKS_API_KEY=your_google_books_api_key
```

Run the application

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

# 📷 Screenshots

There is a separate folder which contains the screenshots.

## ⚙️ How It Works

1. User enters a book title.
2. User selects the summary length.
3. FastAPI receives the request.
4. Google Books API retrieves book details.
5. Gemini AI generates the summary.
6. The summary is saved to SQLite.
7. Results are displayed on the webpage.

---

# 🗄️ Database

SQLite stores:

- Book Name
- Summary Type
- AI Generated Summary
- Timestamp

---

# 🏗️ Architecture

```text
          User

            │

            ▼

      FastAPI Backend

            │

      ┌───────────────┐
      │               │
      ▼               ▼

Google Books API   Gemini AI

      │               │

      └──────┬────────┘

             ▼

     SQLite Database

             ▼

       Jinja2 Templates

             ▼

        Browser
```

---

# 🚀 Future Enhancements

- ⭐ Favorite Books
- 📜 Summary History Dashboard
- 📄 Export Summary as PDF
- ❤️ User Authentication
- 🌙 Dark Mode
- 📈 Analytics Dashboard
- 🔍 Search History
- ☁️ Deploy to Render or Railway
- 🐳 Docker Support

---

# 📖 Learning Outcomes

This project helped me learn:

- FastAPI
- REST API Integration
- Google Gemini API
- Google Books API
- SQLite
- Environment Variables
- Service Layer Architecture
- Jinja2 Templates
- Bootstrap
- Git & GitHub
- Python Project Structure

---

# 👨‍💻 Author

**Shashank Reddy**

GitHub:
https://github.com/shashankreddy92

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
