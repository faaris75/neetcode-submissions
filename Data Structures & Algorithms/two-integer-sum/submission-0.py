class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target-num ## Check for complement first as if you add num first to the hashmap it will fail
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[num]=i
        return []