import unittest
from binarySearch import binarySearch
from linearSearch import linearSearch

class SearchTestCase(unittest.TestCase):
    def testLinearSearch(self):
        values = [1,2,3,4,5,6,7,8,9,10]
        for idx,val in enumerate(values):
            self.assertEqual(idx,linearSearch(values,val))
        self.assertEqual(linearSearch(values,5),4)
        self.assertEqual(linearSearch(values,6),5)
        self.assertEqual(linearSearch(values,0),-1)
        self.assertEqual(linearSearch(values,1),0)
        self.assertEqual(linearSearch(values,2),1)
        self.assertEqual(linearSearch(values,3),2)
        self.assertEqual(linearSearch(values,4),3)
        self.assertEqual(linearSearch(values,10),9)

    def test_binary_search(self):
        values = [2, 5, 20, 90, 99, 100]
        self.assertEqual(binarySearch(values, 2), 0)
        self.assertEqual(binarySearch(values, 5), 1)
        self.assertEqual(binarySearch(values, 20), 2)
        self.assertEqual(binarySearch(values, 100), 5)
        self.assertEqual(binarySearch(values, 99), 4)
        self.assertEqual(binarySearch(values, 90), 3)
    
    if __name__ == '__main__':
        unittest.main()