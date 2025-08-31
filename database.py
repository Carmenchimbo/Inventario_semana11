import sqlite3

def conectar():
    conn = sqlite3.connect("inventario.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            cantidad INTEGER,
            precio REAL
        )
    ''')
    conn.commit()
    return conn
