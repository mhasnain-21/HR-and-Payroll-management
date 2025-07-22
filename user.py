import sqlite3
import bcrypt

DB_FILE = "users.db"

def authenticate(username, password):
    try:
        con = sqlite3.connect(DB_FILE)
        c = con.cursor()
        c.execute("SELECT password FROM users WHERE username=?", (username,))
        row = c.fetchone()
        con.close()

        if row:
            stored_hash = row[0]
            
            # Handle both string and bytes stored hashes
            if isinstance(stored_hash, str):
                stored_hash = stored_hash.encode('utf-8')
            
            # Ensure password is bytes
            if isinstance(password, str):
                password = password.encode('utf-8')
            
            return bcrypt.checkpw(password, stored_hash)
        
        return False
        
    except Exception as e:
        print(f"Authentication error: {e}")
        return False


def get_user_role(username):
    try:
        con = sqlite3.connect(DB_FILE)
        c = con.cursor()
        c.execute("SELECT role FROM users WHERE username=?", (username,))
        row = c.fetchone()
        con.close()
        return row[0] if row else "Unknown"
    except Exception as e:
        print(f"Error getting user role: {e}")
        return "Unknown"


def create_user(username, password, role="user"):
    """Helper function to create a user with properly hashed password"""
    try:
        # Hash the password
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        
        con = sqlite3.connect(DB_FILE)
        c = con.cursor()
        
        # Create users table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password BLOB, role TEXT)''')
        
        # Insert user with hashed password as BLOB
        c.execute("INSERT OR REPLACE INTO users (username, password, role) VALUES (?, ?, ?)", 
                 (username, hashed, role))
        
        con.commit()
        con.close()
        return True
        
    except Exception as e:
        print(f"Error creating user: {e}")
        return False


def initialize_database():
    """Initialize the database with default admin user if needed"""
    try:
        con = sqlite3.connect(DB_FILE)
        c = con.cursor()
        
        # Create users table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password BLOB, role TEXT)''')
        
        # Check if admin user exists
        c.execute("SELECT username FROM users WHERE username=?", ("admin",))
        if not c.fetchone():
            # Create default admin user
            password_bytes = "admin123".encode('utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password_bytes, salt)
            
            c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                     ("admin", hashed, "admin"))
            print("Default admin user created (username: admin, password: admin123)")
        
        con.commit()
        con.close()
        
    except Exception as e:
        print(f"Error initializing database: {e}")


# Initialize database when module is imported
if __name__ == "__main__":
    initialize_database()