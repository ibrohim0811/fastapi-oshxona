import sqlite3


def items():
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    return cur.execute("SELECT * FROM items").fetchall()


def item(item_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    return cur.execute("SELECT * FROM items WHERE id = ?", (item_id, )).fetchone()


def item_create(name: str, about: str, price: int, category_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, about, price, category_id) VALUES (?, ?, ?, ?)")
    conn.commit()
    conn.close()


def item_update(item_id: int, name: str, about: str, is_active: bool, price: int, category_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "UPDATE FROM items (name, about, price, is_active, category_id) SET (?, ?, ?, ?, ?) WHERE id = ?"
    cur.execute(query, (item_id, name, about, price, is_active, category_id))
    conn.commit()
    conn.close()


def item_delete(item_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "DELETE FROM items WHERE id = ?"
    cur.execute(query, (item_id, ))
    conn.commit()
    conn.close()
