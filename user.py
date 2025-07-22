import sqlite3
import bcrypt

DB_FILE = "users.db"

def authenticate(username, password):
    con = sqlite3.connect(DB_FILE)
    c = con.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    row = c.fetchone()
    con.close()

    if row:
        return bcrypt.checkpw(password.encode(),row[0])
    return False

def get_user_role(username):
    con = sqlite3.connect(DB_FILE)
    c = con.cursor()
    c.execute("SELECT role FROM users WHERE username=?",(username,))
    row = c.fetchone()
    con.close()
    return row[0] if row else "Unknown"