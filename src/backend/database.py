"""
Database module for managing user data
"""
import sqlite3


class Database:
    def __init__(self, db_name='test.db'):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        """Initialize database with users table"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT
            )
        ''')
        conn.commit()
        conn.close()
    
    def get_all_users(self):
        """Retrieve all users"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email FROM users')
        users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in cursor.fetchall()]
        conn.close()
        return users
    
    def get_user(self, user_id):
        """Retrieve specific user by ID"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email FROM users WHERE id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {'id': row[0], 'name': row[1], 'email': row[2]}
        return None
    
    def create_user(self, name, email=''):
        """Create a new user"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id
