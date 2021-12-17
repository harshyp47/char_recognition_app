from dummyfunc import dummyfunc
import unittest


class Testing(unittest.TestCase):
    def test_func(self):
        
        self.assertEqual(dummyfunc(3,2), 5)
        self.assertEqual(dummyfunc(5,3), 8)
        self.assertEqual(dummyfunc(1,1), 2)
        self.assertEqual(dummyfunc(2,2), 4)
        self.assertEqual(dummyfunc(3,3), 6)
        self.assertEqual(dummyfunc(4,2), 6)



if __name__ == '__main__':
    unittest.main()

