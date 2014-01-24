import unittest
import sorts

class Test_testsorts(unittest.TestCase):

    def test_bubblesortempty(self):
        unsorted = []
        sorted = []
        self.assertEqual(sorted, sorts.bubblesort(unsorted))

    def test_bubblesortsimple(self):
        unsorted = [3,2,4,5,1]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, sorts.bubblesort(unsorted))

    def test_bubblesortsorted(self):
        unsorted = [1,2,3,4,5]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, sorts.bubblesort(unsorted))
        
    def test_bubblesortreversed(self):
        unsorted = [5,4,3,2,1]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, sorts.bubblesort(unsorted))

    def test_bubblesortduplicates(self):
        unsorted = [3,2,1,2,4]
        sorted = [1,2,2,3,4]
        self.assertEqual(sorted, sorts.bubblesort(unsorted))



if __name__ == '__main__':
    unittest.main()
