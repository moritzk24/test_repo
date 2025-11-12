"""
Unit tests for the database module
"""
import unittest
import os
from src.backend.database import Database


class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        """Set up test database"""
        self.test_db = 'test_users.db'
        self.db = Database(self.test_db)
    
    def tearDown(self):
        """Clean up test database"""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
    
    def test_create_user(self):
        """Test user creation"""
        user_id = self.db.create_user("John Doe", "john@example.com")
        self.assertIsNotNone(user_id)
        self.assertGreater(user_id, 0)
    
    def test_get_user(self):
        """Test retrieving a user"""
        user_id = self.db.create_user("Jane Doe", "jane@example.com")
        user = self.db.get_user(user_id)
        self.assertIsNotNone(user)
        self.assertEqual(user['name'], "Jane Doe")
        self.assertEqual(user['email'], "jane@example.com")
    
    def test_get_all_users(self):
        """Test retrieving all users"""
        self.db.create_user("User 1", "user1@example.com")
        self.db.create_user("User 2", "user2@example.com")
        users = self.db.get_all_users()
        self.assertEqual(len(users), 2)


if __name__ == '__main__':
    unittest.main()
