import sqlite3

def get_connection():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    return conn

def init_db(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS lists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                deadline TEXT,
                completed INTEGER DEFAULT 0,
                list_id INTEGER DEFAULT NULL,
                FOREIGN KEY (list_id) REFERENCES lists (id)
            )
        ''')

