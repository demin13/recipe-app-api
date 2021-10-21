from django.test import TestCase

from .calc import add, subtract, multiply, divide


class CalcTests(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(12, 3), 15)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(15, 3), 12)
    
    def test_multiply_numbers(self):
        self.assertEqual(multiply(3, 5), 15)
    
    def test_divide_numbers(self):
        self.assertEqual(divide(15, 5), 3)
