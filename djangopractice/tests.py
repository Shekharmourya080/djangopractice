from django.test import TestCase

from djangopractice.calc import add, sub


class CalculatorTest(TestCase):

    def test_addition_of_two_number(self):
        """THis test case will test two number success"""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_numbers(self):
        """this test case will test two number """
        self.assertEqual(sub(6, 5), 1)
