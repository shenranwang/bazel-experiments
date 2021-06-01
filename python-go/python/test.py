import unittest
import importlib

main = importlib.import_module("hello-world")

class TestSquare(unittest.TestCase):
    def test_helloworld1(self):
        self.assertIn("Squared 3 -> 9\n", main.square(3))

    def test_helloworld2(self):
        self.assertIn("Squared 10 -> 100\n", main.square(10))

if __name__ == '__main__':
    unittest.main()