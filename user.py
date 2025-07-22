import sqlite3

# Initialize the users database and create the users table
def init_user_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Add a new user
def add_user(username, password, role):
    if user_exists(username):
        return False  # User already exists
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                (username, password, role))
    conn.commit()
    conn.close()
    return True

# Check if a user exists
def user_exists(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

# Authenticate user credentials
def authenticate(username, password):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()
    conn.close()
    return user is not None

# Get user role by username
def get_user_role(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT role FROM users WHERE username = ?", (username,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None
