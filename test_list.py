import unittest
import list

class testList(unittest.TestCase):
    def test1(self):
        self.assertEqual(list.average([1, 2, 3]), 2)
        
    def test2(self):
        self.assertEqual(list.average([-1, -2, -3, -4]), -2.5)
        
    def test3(self):
        self.assertEqual(list.average([]), 0)


if __name__ == '__main__':
    unittest.main()