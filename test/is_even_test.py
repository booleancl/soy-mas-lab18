import unittest
import importlib

from functions.is_even import is_even

class TestSuite(unittest.TestCase):
    def test_is_even(self):
        assert is_even(4200)
        assert is_even(333) == False
