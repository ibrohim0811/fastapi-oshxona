import sqlite3


def create_table():
    conn = sqlite3.connect("oshxona.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200)
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customer(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(200),
        last_name VARCHAR(200),
        email TEXT UNIQUE 
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(200) NOT NULL,
        about TEXT,
        price INTEGER,
        is_active BOOLEAN DEFAULT TRUE,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
            ON DELETE CASCADE
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status VARCHAR(100) DEFAULT 'pending',
        customer_id INTEGER NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customer(id)
            ON DELETE CASCADE
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        menu_item_id INTEGER, 
        
        FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
        FOREIGN KEY (menu_item_id) REFERENCES items(id) ON DELETE CASCADE
    );
    """)
    conn.commit()
    conn.close()