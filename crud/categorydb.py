import sqlite3


def categories():
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "SELECT * FROM categories"
    return cur.execute(query).fetchall()


def category_detail(id):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    insert = "SELECT * FROM categories WHERE id = ?"
    return cur.execute(insert, (id, )).fetchone()


def category_create(category_name: str):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "INSERT INTO categories (name) VALUES (?)"
    cur.execute(query, (category_name, ))
    conn.commit()
    conn.close()


def category_update(id: int, category_name: str):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "UPDATE categories SET name = ? WHERE id = ?"
    cur.execute(query, (id, category_name))
    conn.commit()
    conn.close()


def category_delete(id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "DELETE FROM categories WHERE id = ?"
    cur.execute(query, (id, ))
    conn.commit()
    conn.close()
