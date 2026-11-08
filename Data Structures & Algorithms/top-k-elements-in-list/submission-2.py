class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        topk = sorted(d, key = lambda x: d[x], reverse = True)[:k]
        return topk

        ## Can also use key = d.get to sort the values 