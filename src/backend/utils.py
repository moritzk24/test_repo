"""
Utility functions for the application
"""
from datetime import datetime


def format_response(data, status_code):
    """Format API response with standard structure"""
    return {
        'status': status_code,
        'data': data,
        'timestamp': datetime.utcnow().isoformat()
    }


def validate_email(email):
    """Basic email validation"""
    if not email:
        return False
    return '@' in email and '.' in email


def log_message(message, level='INFO'):
    """Simple logging function"""
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] {level}: {message}")
