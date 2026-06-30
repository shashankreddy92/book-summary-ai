from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from services.ai_service import summarize_book

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/summary")
def summary(
    request: Request,
    book_name: str = Form(...),
    summary_type: str = Form(...)
):

    summary_text = summarize_book(
        book_name,
        summary_type
    )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "request": request,
            "book_name": book_name,
            "summary": summary_text,
            "summary_type": summary_type
        }
    )