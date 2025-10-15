# test_samzapipeline.py
"""
Tests for SamzaPipeline module.
"""

import unittest
from samzapipeline import SamzaPipeline

class TestSamzaPipeline(unittest.TestCase):
    """Test cases for SamzaPipeline class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SamzaPipeline()
        self.assertIsInstance(instance, SamzaPipeline)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SamzaPipeline()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
