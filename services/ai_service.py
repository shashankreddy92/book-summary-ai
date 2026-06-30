import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def summarize_book(book_name, summary_type):

    prompt = f"""
    You are a helpful book summarization assistant.

    Generate a {summary_type} summary for the book:

    {book_name}

    If the book is well known,
    generate an accurate summary.

    If the book is unknown,
    politely say that the book could not be found.

    Keep the response clean and easy to read.
    """

    response = model.generate_content(prompt)

    return response.text