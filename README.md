# Test Repository

A simple test repository for testing Software Composition Analysis (SCA) tools and repository analyzers.

## Project Structure

This is a basic web application with a Python Flask backend and Node.js Express frontend.

```
test_repo/
├── src/
│   ├── backend/         # Python Flask API
│   │   ├── app.py       # Main Flask application
│   │   ├── database.py  # Database operations
│   │   └── utils.py     # Utility functions
│   └── frontend/        # Node.js Express frontend
│       └── app.js       # Frontend server
├── tests/               # Unit tests
│   ├── test_utils.py
│   └── test_database.py
├── config.yaml          # Application configuration
├── requirements.txt     # Python dependencies
└── package.json         # Node.js dependencies
```

## Dependencies

### Backend (Python)
- Flask 2.3.0
- Requests 2.31.0
- SQLAlchemy 2.0.0
- Python-dotenv 1.0.0
- Werkzeug 2.3.0

### Frontend (Node.js)
- Express 4.18.2
- Axios 1.4.0
- Lodash 4.17.21

## Installation

### Backend Setup
```bash
pip install -r requirements.txt
```

### Frontend Setup
```bash
npm install
```

## Running the Application

### Start Backend
```bash
cd src/backend
python app.py
```

### Start Frontend
```bash
npm start
```

## Testing

Run Python tests:
```bash
python -m pytest tests/
```

## Features

- RESTful API with Flask
- SQLite database integration
- Express frontend proxy server
- User management endpoints
- Basic validation and error handling

## API Endpoints

- `GET /` - Home endpoint
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get specific user
- `POST /api/users` - Create new user

## Purpose

This repository is designed to test:
- Dependency scanning
- Vulnerability detection
- Code quality analysis
- Repository structure analysis
- Package management tools
