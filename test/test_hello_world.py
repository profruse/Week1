import unittest
from main_source_code import hello_world as hello


class MyTestCase(unittest.TestCase):
    def test_print_message(self):
        self.assertEqual('Hello!', hello.message())


if __name__ == '__main__':
    unittest.main()
