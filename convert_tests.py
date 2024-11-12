import unittest
from convert import str_to_float
from command_line import do_sum

class TestConvert(unittest.TestCase):
    def test_str_to_float1(self):
        self.assertEqual(str_to_float("120.1234"), 120.1234)

    def test_str_to_float2(self):
        self.assertEqual(str_to_float("hello"), None)

    def test_do_sum1(self):
        p = "1.5 2.2"
        self.assertEqual(do_sum(p), 3.7)

    def test_do_sum2(self):
        p = "5 8.9 hello 9.1 5000"
        self.assertEqual(do_sum(p), 5023.0)