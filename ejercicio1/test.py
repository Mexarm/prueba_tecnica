import unittest
from script import get_greatest


class TestEjercicio1(unittest.TestCase):

    def test_case1(self):
        self.assertEqual(get_greatest('283910', 2), 91)

    def test_case2(self):
        self.assertEqual(get_greatest('1234567890', 5), 67890)


if __name__ == '__main__':
    unittest.main()
