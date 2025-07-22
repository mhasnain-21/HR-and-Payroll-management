# create_users_db.py
import sqlite3
import bcrypt

con = sqlite3.connect("users.db")
cur = con.cursor()

# Create table
cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, role TEXT)")

# Add an admin user
username = "admin"
password = "admin123"
hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hashed_pw, "Admin"))

con.commit()
con.close()

print("✅ users.db created with username=admin, password=admin123")
