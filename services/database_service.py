
import sqlite3

conn = sqlite3.connect("database/books.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM books")
print(cursor.fetchone())

conn.close()

DATABASE = "database/books.db"


def create_table():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            book_name TEXT NOT NULL,

            summary_type TEXT NOT NULL,

            summary TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


def save_summary(book_name, summary_type, summary):
    print("=" * 50)
    print("Saving summary to database...")
    print("Book Name:", book_name)
    print("Summary Type:", summary_type)

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO books
        (book_name, summary_type, summary)
        VALUES (?, ?, ?)
    """, (
        book_name,
        summary_type,
        summary
    ))

    conn.commit()

    print("Rows inserted:", cursor.rowcount)
    print("Last inserted ID:", cursor.lastrowid)

    conn.close()

    print("Saved successfully!")
    print("=" * 50)


def get_summary_by_id(book_id):
    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM books
        WHERE id = ?
    """, (book_id,))

    row = cursor.fetchone()

    conn.close()

    return row


def delete_summary(book_id):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM books
        WHERE id = ?
    """, (book_id,))

    conn.commit()

    conn.close()