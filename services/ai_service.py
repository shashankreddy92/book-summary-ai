def summarize_book(book_name, summary_type):

    if summary_type == "short":
        return f"""
This is a short summary of "{book_name}".

This feature is currently a placeholder.
Soon an AI model will generate an actual summary.
"""

    elif summary_type == "medium":
        return f"""
This is a medium-length summary of "{book_name}".

The application currently demonstrates how different summary
lengths will be displayed.

Later we will integrate an AI model to generate real summaries.
"""

    elif summary_type == "detailed":
        return f"""
This is a detailed summary of "{book_name}".

Future versions of this application will use an AI model
to generate detailed chapter-wise summaries, key ideas,
important lessons, and takeaways.

This is currently sample text.
"""

    return "Summary not available."