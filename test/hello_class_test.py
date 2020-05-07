import unittest

from src.hello_class import HelloClass


class HelloClassTest(unittest.TestCase):
    
    def test_say_hello_db1(self):
        expected = "Hello DB1 !"
        instance = HelloClass("DB1")
        self.assertEqual(expected, instance.say_hello())


if __name__ == '__main__':
    unittest.main()
