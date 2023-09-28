import unittest

def name():
    x = 'jose'
    return x.upper()

class Checker(unittest.TestCase):

    def test_name(self):
        self.assertEqual(name(), 'PEDRO')

if __name__ == '__main__':
    unittest.main()