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


def sanitize_string(text):
    """Remove potentially harmful characters from input"""
    if not text:
        return ""
    return text.strip().replace('<', '').replace('>', '')


def log_message(message, level='INFO'):
    """Simple logging function"""
    timestamp = datetime.utcnow().isoformat()
    print(f"[{timestamp}] {level}: {message}")


def calculate_age(birth_year):
    """Calculate age from birth year"""
    current_year = datetime.now().year
    return current_year - birth_year
