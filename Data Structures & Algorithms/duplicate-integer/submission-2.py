class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                return True
            hash_map[num] = i
        return False
    