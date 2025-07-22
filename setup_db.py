import sqlite3
import bcrypt

con = sqlite3.connect("users.db")
c = con.cursor()
users = [("admin", "admin123", "Admin"), ("hrmanager", "hr2025", "HR"),
         ("payrollstaff", "payroll2025", "Payroll")]

for username, pwd, role in users:
    hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
    try:
        c.execute("INSERT INTO users (username, password, role) Values (?,?,?)", (username, hashed, role))
    except sqlite3.IntegrityError:
        pass

con.commit()
con.close()
