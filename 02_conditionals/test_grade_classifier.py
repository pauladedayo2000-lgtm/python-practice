import unittest
from grade_classifier import classify_score


class TestClassifyScore(unittest.TestCase):
    def test_boundaries(self):
        cases = {100: "A", 70: "A", 69: "B", 60: "B", 59: "C", 50: "C",
                 49: "D", 45: "D", 44: "E", 40: "E", 39: "F", 0: "F"}
        for score, expected in cases.items():
            with self.subTest(score=score):
                self.assertEqual(classify_score(score), expected)

    def test_out_of_range(self):
        for bad_score in (-1, 101):
            with self.subTest(score=bad_score):
                with self.assertRaises(ValueError):
                    classify_score(bad_score)


if __name__ == "__main__":
    unittest.main(exit=False)
