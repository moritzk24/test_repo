"""
Main application entry point for Flask backend
"""
from flask import Flask, jsonify, request
from database import Database
from utils import format_response

app = Flask(__name__)
db = Database()


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify(format_response("Welcome to TestApp API", 200))


@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = db.get_all_users()
    return jsonify(format_response(users, 200))


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get specific user by ID"""
    user = db.get_user(user_id)
    if user:
        return jsonify(format_response(user, 200))
    return jsonify(format_response("User not found", 404)), 404


@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify(format_response("Invalid data", 400)), 400
    
    user_id = db.create_user(data['name'], data.get('email', ''))
    return jsonify(format_response({"id": user_id, "name": data['name']}, 201)), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
