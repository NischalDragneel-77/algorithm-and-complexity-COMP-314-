import unittest
from insertionSort import insertion_sort
from mergeSort import merge_sort

class sortingTestCase(unittest.TestCase):
    def test_insertion(self):
        A = [3,2,1,5,7]
        B = [1,2,3,5,7]
        C = [7,5,3,2,1]
        sortedA = [1,2,3,5,7]
        insertion_sort(A)
        insertion_sort(B)
        insertion_sort(C)
        self.assertListEqual(A,sortedA)
        self.assertListEqual(B,sortedA)
        self.assertListEqual(C,sortedA)
    
    def test_merge(self):
        A = [3,2,1,5,7]
        B = [1,2,3,5,7]
        C = [7,5,3,2,1]
        sortedA = [1,2,3,5,7]
        merge_sort(A,0,4)
        merge_sort(B,0,4)
        merge_sort(C,0,4)
        self.assertListEqual(A,sortedA)
        self.assertListEqual(B,sortedA)
        self.assertListEqual(C,sortedA)

if __name__ == '__main__':
    unittest.main()