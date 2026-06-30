import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")


def get_book_details(book_name):
    
    url = (
        "https://www.googleapis.com/books/v1/volumes"
        f"?q={book_name}"
        "&maxResults=1"
        f"&key={API_KEY}"
    )

    print("URL:", url)

    response = requests.get(url)

    print("Status Code:", response.status_code)

    data = response.json()

    print(data)

    if "items" not in data:
        return None

    book = data["items"][0]["volumeInfo"]

    return {
        "title": book.get("title", "N/A"),
        "authors": ", ".join(book.get("authors", ["Unknown"])),
        "publisher": book.get("publisher", "Unknown"),
        "publishedDate": book.get("publishedDate", "Unknown"),
        "description": book.get("description", "No description available."),
        "thumbnail": book.get("imageLinks", {}).get("thumbnail", ""),
        "rating": book.get("averageRating", "N/A")
    }