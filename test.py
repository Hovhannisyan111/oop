from script import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_split(self):
        s = "hello world"
        self.assertEqual(my_split(s), ["hello", "world"])
        with self.assertRaises(TypeError):
            my_split(2)

    def test_upper(self):
        self.assertEqual(my_upper("hello world"), "HELLO WORLD")

    def test_reverse(self):
        self.assertEqual(my_reverse("hello"), "olleh")

if __name__ == "__main__":
    unittest.main()
