import sqlite3


def orders():
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    return cur.execute("SELECT * FROM orders").fetchall()


def order(order_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    return cur.execute("SELECT * FROM orders WHERE id = ?", (order_id, )).fetchone()


def order_create(status: str, customer_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO orders (status, customer_id) VALUES (?, ?)", (status, customer_id))
    conn.commit()
    conn.close()


def order_update(order_id: int, status: str, customer_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "UPDATE orders SET status = ?, customer_id = ? WHERE id = ?"
    cur.execute(query, (status, customer_id, order_id))
    conn.commit()
    conn.close()


def order_delete(order_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "DELETE FROM orders WHERE id = ?"
    cur.execute(query, (order_id, ))
    conn.commit()
    conn.close()
