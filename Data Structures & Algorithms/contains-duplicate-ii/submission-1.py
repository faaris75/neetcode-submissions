class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashmap = {}
        l,r = 0,0

        for i, num in enumerate(nums):
            if num in hashmap and abs(i-hashmap[num])<= k:
                return True
            hashmap[num] = i
        return False
                
        