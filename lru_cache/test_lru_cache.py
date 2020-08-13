import unittest
from lru_cache import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)

    def test_cache_overwrite_appropriately(self):
        self.cache.set_pair('item1', 'a')
        self.cache.set_pair('item2', 'b')
        self.cache.set_pair('item3', 'c')

        self.cache.set_pair('item2', 'z')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item2'), 'z')

    def test_cache_insertion_and_retrieval(self):
        self.cache.set_pair('item1', 'a')
        self.cache.set_pair('item2', 'b')
        self.cache.set_pair('item3', 'c')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.cache.set_pair('item4', 'd')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.assertEqual(self.cache.get('item3'), 'c')
        self.assertEqual(self.cache.get('item4'), 'd')
        self.assertIsNone(self.cache.get('item2'))

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent'))


if __name__ == '__main__':
    unittest.main()

 while nums:
            i = nums.pop()
            test = len(nums)
            nums = [j for j in nums if j != i]
            if len(nums) == test:
                return i