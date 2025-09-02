import sqlite3

# Get database connection
def get_database_connection(db_name = "todo.db"):
    return sqlite3.connect(db_name)

# Create tables 
def init_db(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0,
        category TEXT
    )
    ''')
    conn.commit()
