import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS book(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            publisher TEXT,
            collection TEXT,
            pages INTEGER,
            translator TEXT,
            edition TEXT,
            first_edition INTEGER,
            print_year INTEGER,
            isbn TEXT
        )
    """)
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", publisher="", collection="", pages="", translator="", edition="", first_edition="", print_year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM book WHERE 
        title = ? OR author = ? OR publisher = ? OR collection = ? OR
        pages = ? OR translator = ? OR edition = ? OR first_edition = ? OR
        print_year = ? OR isbn = ?
    """, (title, author, publisher, collection, pages, translator, edition, first_edition, print_year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def insert(title, author, publisher, collection, pages, translator, edition, first_edition, print_year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO book VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (title, author, publisher, collection, pages, translator, edition, first_edition, print_year, isbn))
    conn.commit()
    conn.close()

def update(id, title="", author="", publisher="", collection="", pages="", translator="", edition="", first_edition="", print_year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
        UPDATE book SET 
        title = ?, author = ?, publisher = ?, collection = ?, pages = ?,
        translator = ?, edition = ?, first_edition = ?, print_year = ?, isbn = ?
        WHERE id = ?
    """, (title, author, publisher, collection, pages, translator, edition, first_edition, print_year, isbn, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

connect()
print(view())


#insert("The Sun", "John Smith", "XYZ Publishing", "Nature Series", 250, "Alice Johnson", "First", 1915, 1920, "121-203-91")
#delete(3)
#update(4, "The Moon", "John Smooth", "ABC Publishing", "Space Collection", 320, "Bob Williams", "Second", 1917, 1921, 999999999)
#print(search(author="John Smith"))