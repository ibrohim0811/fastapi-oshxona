import sqlite3


def customers():
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    return cur.execute("SELECT * FROM customer").fetchall()


def customer(customer_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    return cur.execute("SELECT * FROM customer WHERE id = ?", (customer_id, )).fetchone()


def customer_create(first_name: str, last_name: str, email: str):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO customer (first_name, last_name, email) VALUES (?, ?, ?)", (first_name, last_name, email))
    conn.commit()
    conn.close()


def customer_update(customer_id: int, first_name: str, last_name: str, email: str):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    query = "UPDATE customer SET first_name = ?, last_name = ?, email = ? WHERE id = ?"    
    cur.execute(query, (first_name, last_name, email, customer_id))
    conn.commit()
    conn.close()


def customer_delete(customer_id: int):
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM customer WHERE id = ?", (customer_id, ))
    conn.commit()
    conn.close()

