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
    
    def test_update_user(self):
        """Test updating a user"""
        user_id = self.db.create_user("Old Name", "old@example.com")
        self.db.update_user(user_id, "New Name", "new@example.com")
        user = self.db.get_user(user_id)
        self.assertEqual(user['name'], "New Name")
        self.assertEqual(user['email'], "new@example.com")
    
    def test_delete_user(self):
        """Test deleting a user"""
        user_id = self.db.create_user("Delete Me", "delete@example.com")
        self.db.delete_user(user_id)
        user = self.db.get_user(user_id)
        self.assertIsNone(user)
    
    def test_get_nonexistent_user(self):
        """Test retrieving a user that doesn't exist"""
        user = self.db.get_user(99999)
        self.assertIsNone(user)
    
    def test_create_user_with_empty_name(self):
        """Test creating user with empty name"""
        with self.assertRaises(ValueError):
            self.db.create_user("", "test@example.com")
    
    def test_create_user_with_invalid_email(self):
        """Test creating user with invalid email"""
        with self.assertRaises(ValueError):
            self.db.create_user("Test User", "invalid-email")
    
    def test_duplicate_email(self):
        """Test that duplicate emails are handled"""
        self.db.create_user("User 1", "same@example.com")
        with self.assertRaises(ValueError):
            self.db.create_user("User 2", "same@example.com")
    
    def test_get_all_users_empty_database(self):
        """Test retrieving all users from empty database"""
        users = self.db.get_all_users()
        self.assertEqual(len(users), 0)
        self.assertIsInstance(users, list)
    
    def test_user_count(self):
        """Test counting users in database"""
        self.assertEqual(self.db.count_users(), 0)
        self.db.create_user("User 1", "user1@example.com")
        self.assertEqual(self.db.count_users(), 1)
        self.db.create_user("User 2", "user2@example.com")
        self.assertEqual(self.db.count_users(), 2)


if __name__ == '__main__':
    unittest.main()
