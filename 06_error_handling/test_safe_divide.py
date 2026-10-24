import unittest
from safe_divide import safe_divide


class TestSafeDivide(unittest.TestCase):
    def test_normal_division(self):
        self.assertEqual(safe_divide(10, 2), 5)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(safe_divide(1, 0))

    def test_wrong_type_returns_none(self):
        self.assertIsNone(safe_divide("a", 2))


if __name__ == "__main__":
    unittest.main(exit=False)
