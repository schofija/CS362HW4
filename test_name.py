import unittest
import name

class testName(unittest.TestCase):
    def test1(self):
        self.assertEqual(name.fullname("Dennis", "Reynolds"), "Dennis Reynolds")
        
    def test2(self):
        self.assertEqual(name.fullname(5, 5), "5 5")
        
    def test3(self):
        self.assertEqual(name.fullname("", ""), " ")


if __name__ == '__main__':
    unittest.main()