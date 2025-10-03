# test_parcelbundler.py
"""
Tests for ParcelBundler module.
"""

import unittest
from parcelbundler import ParcelBundler

class TestParcelBundler(unittest.TestCase):
    """Test cases for ParcelBundler class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ParcelBundler()
        self.assertIsInstance(instance, ParcelBundler)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ParcelBundler()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
