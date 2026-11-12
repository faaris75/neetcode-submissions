class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # set(nums) is a slightly faster/cleaner way to remove duplicates
        newnum = sorted(list(set(nums))) 
        n = len(newnum) - 1
        
        longest = 1
        counter = 1

        for i in range(n):
            if newnum[i+1] - newnum[i] == 1:
                counter += 1
            else:
                # Sequence broke. Save the highest count, then reset counter.
                longest = max(longest, counter)
                counter = 1
                
        # Return the max of 'longest' and the final 'counter' 
        # (in case the longest sequence is at the very end of the list)
        return max(longest, counter)