import unittest
import importlib

from functions.void_return import sum
from functions.void_return import substract
from functions.void_return import multiply
from functions.void_return import division

class TestSuite(unittest.TestCase):
    def test_operations(self):
        assert sum(25, 35) == 60
        assert substract(33,3) == 30
        assert multiply(25, 5) == 125
        assert division(30, 3) == 10
