def summarize_book(book_name, summary_type):

    if summary_type == "short":
        return f"Short summary of {book_name}"

    elif summary_type == "medium":
        return f"Medium summary of {book_name}"

    elif summary_type == "detailed":
        return f"Detailed summary of {book_name}"

    return "Summary not available."