class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target-num
            if complement in hashmap:
                return [hashmap[complement],i]      # I did hashmap[num]
            else:
                hashmap[num]=i          # I did hashmap.append(i)
        return []
    