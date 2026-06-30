from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from services.ai_service import summarize_book
from services.book_service import get_book_details
from services.database_service import create_table, save_summary

# Create FastAPI app
app = FastAPI()

# Create database and table on startup
create_table()

# Jinja templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/summary", response_class=HTMLResponse)
def summary(
    request: Request,
    book_name: str = Form(...),
    summary_type: str = Form(...)
):
    # Generate AI Summary
    summary_text = summarize_book(
        book_name,
        summary_type
    )

    # Save summary to SQLite database
    save_summary(
        book_name,
        summary_type,
        summary_text
    )

    # Fetch book details
    book = get_book_details(book_name)

    # Debug (optional)
    print("BOOK DATA:")
    print(book)

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "book_name": book_name,
            "summary": summary_text,
            "summary_type": summary_type,
            "book": book
        }
    )