from version_control import encode
import unittest


class MyTestCase(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("12345555"), "45678888")
        self.assertEqual(encode("00009962"), "33332295")


if __name__ == '__main__':
    unittest.main()
