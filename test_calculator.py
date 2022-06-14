import unittest
from calculator import MemoryCalculator


class TestMemoryCalculator(unittest.TestCase):
    def test_sum_is_zero_on_initialization(self):
        calculator = MemoryCalculator()
        self.assertEqual(0, calculator.sum())

    def test_sum_one_number(self):
        calculator = MemoryCalculator()
        calculator.add(5)
        self.assertEqual(5, calculator.sum())

    def test_sum_two_numbers(self):
        calculator = MemoryCalculator()
        calculator.add(5)
        calculator.add(5)
        self.assertEqual(10, calculator.sum())

    def test_sub_one_number(self):
        calculator = MemoryCalculator()
        calculator.add(15)
        calculator.sub(5)
        self.assertEqual(10, calculator.sum())

    def test_multiply_one_number(self):
        calculator = MemoryCalculator()
        calculator.add(5)
        calculator.multiply(5)
        self.assertEqual(25, calculator.sum())

    def test_sum_two_numbers(self):
        calculator = MemoryCalculator()
        calculator.add(5)
        calculator.divide(5)
        self.assertEqual(1, calculator.sum())

    def test_sum_is_zero_after_calling_sum(self):
        calculator = MemoryCalculator()
        calculator.add(5)
        calculator.add(5)
        calculator.sum()
        self.assertEqual(0, calculator.sum())

    def test_sum_numbers_and_save_last_sum(self):
        calculator = MemoryCalculator()
        calculator._save_last_sum = True
        calculator.add(5)
        calculator.add(5)
        calculator.sum()
        calculator.add(5)
        x = calculator.last_sum
        self.assertEqual(15, x + calculator.sum())
 
    def test_operation_complete(self):
        calculator = MemoryCalculator()
        calculator.add(50)
        calculator.divide(5)
        calculator.multiply(3)
        calculator.sub(3)
        self.assertEqual(27, calculator.sum())