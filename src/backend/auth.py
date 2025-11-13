"""
Authentication module for user management
"""
import hashlib
import secrets
from datetime import datetime, timedelta


class AuthenticationManager:
    """Handles user authentication and session management"""
    
    def __init__(self):
        self.sessions = {}
        self.users = {}
    
    def hash_password(self, password: str, salt: str = None) -> tuple:
        """Hash a password with a salt"""
        if salt is None:
            salt = secrets.token_hex(16)
        
        pwd_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return pwd_hash.hex(), salt
    
    def register_user(self, username: str, password: str, email: str) -> bool:
        """Register a new user"""
        if username in self.users:
            return False
        
        pwd_hash, salt = self.hash_password(password)
        self.users[username] = {
            'password_hash': pwd_hash,
            'salt': salt,
            'email': email,
            'created_at': datetime.now()
        }
        return True
    
    def authenticate(self, username: str, password: str) -> str:
        """Authenticate a user and return a session token"""
        if username not in self.users:
            return None
        
        user = self.users[username]
        pwd_hash, _ = self.hash_password(password, user['salt'])
        
        if pwd_hash == user['password_hash']:
            token = secrets.token_urlsafe(32)
            self.sessions[token] = {
                'username': username,
                'expires_at': datetime.now() + timedelta(hours=24)
            }
            return token
        
        return None
    
    def validate_session(self, token: str) -> str:
        """Validate a session token and return username if valid"""
        if token not in self.sessions:
            return None
        
        session = self.sessions[token]
        if datetime.now() > session['expires_at']:
            del self.sessions[token]
            return None
        
        return session['username']
    
    def logout(self, token: str) -> bool:
        """Invalidate a session token"""
        if token in self.sessions:
            del self.sessions[token]
            return True
        return False
