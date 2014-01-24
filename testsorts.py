import unittest
import sorts

class Test_bubblesort(unittest.TestCase):
    def setUp(self):
        self.sortfunction = sorts.bubblesort

    def test_empty(self):
        unsorted = []
        sorted = []
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_simple(self):
        unsorted = [3,2,4,5,1]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_sorted(self):
        unsorted = [1,2,3,4,5]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, self.sortfunction(unsorted))
        
    def test_reversed(self):
        unsorted = [5,4,3,2,1]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_duplicates(self):
        unsorted = [3,2,1,2,4]
        sorted = [1,2,2,3,4]
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_letters(self):
        unsorted = ['c','b','d','e','a']
        sorted = ['a','b','c','d','e']
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_negatives(self):
        unsorted = [3, -1, 0, -4, 2]
        sorted = [-4, -1, 0, 2, 3]
        self.assertEqual(sorted, self.sortfunction(unsorted))

class Test_mergesort(unittest.TestCase):
    def setUp(self):
        self.sortfunction = sorts.mergesort

    def test_empty(self):
        unsorted = []
        sorted = []
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_simple(self):
        unsorted = [3,2,4,5,1]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_sorted(self):
        unsorted = [1,2,3,4,5]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, self.sortfunction(unsorted))
        
    def test_reversed(self):
        unsorted = [5,4,3,2,1]
        sorted = [1,2,3,4,5]
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_duplicates(self):
        unsorted = [3,2,1,2,4]
        sorted = [1,2,2,3,4]
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_letters(self):
        unsorted = ['c','b','d','e','a']
        sorted = ['a','b','c','d','e']
        self.assertEqual(sorted, self.sortfunction(unsorted))

    def test_negatives(self):
        unsorted = [3, -1, 0, -4, 2]
        sorted = [-4, -1, 0, 2, 3]
        self.assertEqual(sorted, self.sortfunction(unsorted))

class Test_merge(unittest.TestCase):
    def test_mergeempties(self):
        first = []
        second = []
        merged = []
        self.assertEqual(merged, sorts.merge(first,second))

    def test_mergeoneemptylist(self):
        first = []
        second = [1,2,3]
        merged = [1,2,3]
        self.assertEqual(merged, sorts.merge(first, second))

    def test_mergeotheremptylist(self):
        first = [1,2,3]
        second = []
        merged = [1,2,3]
        self.assertEqual(merged, sorts.merge(first, second))

    def test_merge_balanced_lists(self):
        first = [1,3,4]
        second = [2,5,6]
        merged = [1,2,3,4,5,6]
        self.assertEqual(merged, sorts.merge(first,second))

    def test_merge_unbalanced_lists(self):
        first = [1,3,4,6]
        second = [2,5]
        merged = [1,2,3,4,5,6]
        self.assertEqual(merged, sorts.merge(first,second))


if __name__ == '__main__':
    unittest.main()
