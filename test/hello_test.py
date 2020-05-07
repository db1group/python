import unittest

from src.hello import hello


class HelloTest(unittest.TestCase):
    def test_say_hello_db1(self):
        expected = "Hello DB1 !"
        result = hello.say_hello("DB1")
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
