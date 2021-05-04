import unittest
import cube

class testCube(unittest.TestCase):
    def test1(self):
        self.assertEqual(cube.volume(3), 27)
        
    def test2(self):
        self.assertEqual(cube.volume("a"), 0)
        
    def test3(self):
        self.assertEqual(cube.volume(-5), 0)


if __name__ == '__main__':
    unittest.main()