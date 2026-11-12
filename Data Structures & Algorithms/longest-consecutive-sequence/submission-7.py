class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: # Checks edge cases if empty return 0
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

        # n(logn) is the runtime complexity and the space complexity is o(n)


        '''
        OLD OWN SOLUTION WHICH ONLY WORKS FOR CASE 1
        class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newnum = sorted(list(dict.fromkeys(nums)))  # Removes duplicates then sort it
        n = len(newnums)-1
        counter = 1

        for i in range(n):
            if (newnum[i+1] - newnum[i] == 1):
                counter += 1
                continue
            return counter
        return 0

        # This solution doens't take note of the fact that a second consequetive sequnce can starts after the if statement is false for eg (1,2,3,6,7,8,9) this solution would return 3 which is wrong




        '''