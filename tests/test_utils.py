"""
Unit tests for the utils module
"""
import unittest
from src.backend.utils import format_response, validate_email, log_message


class TestUtils(unittest.TestCase):
    
    def test_format_response(self):
        """Test response formatting"""
        result = format_response("test data", 200)
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['data'], "test data")
        self.assertIn('timestamp', result)
    
    def test_validate_email_valid(self):
        """Test email validation with valid email"""
        self.assertTrue(validate_email("test@example.com"))
    
    def test_validate_email_invalid(self):
        """Test email validation with invalid email"""
        self.assertFalse(validate_email("invalid"))
        self.assertFalse(validate_email(""))
    
    def test_log_message(self):
        """Test logging function"""
        # This test just ensures the function runs without error
        log_message("Test message", "INFO")
        log_message("Error message", "ERROR")


if __name__ == '__main__':
    unittest.main()
