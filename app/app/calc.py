from django.test import TestCase

from .calc import add


class CalcTest(TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 10)