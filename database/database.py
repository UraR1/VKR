import sqlite3

DB_PATH = "database/my_epilemob.db"

def connect():
    return sqlite3.connect(DB_PATH)

def setup_db():
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patient (id INTEGER PRIMARY KEY, name TEXT, birth_date TEXT, sex TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS seizure (id INTEGER PRIMARY KEY, patient_name TEXT, seizure_start TEXT, seizure_duration INTEGER, seizure_type TEXT)''')
        # ... Additional table creation here
        connection.commit()

def create_user(username, password):
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        connection.commit()

def validate_login(username, password):
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
    return user is not None

def is_username_available(username: str) -> bool:
    with connect() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM user WHERE username = ?", (username,))
        return cursor.fetchone() is None