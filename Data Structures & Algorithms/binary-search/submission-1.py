class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while(l<=r):            # I did l<r initially which doesn't check the last answer
            m = (r+l)//2       # must be // instead of / or it will return float for m
            if(nums[m]==target):
                return m
            elif(nums[m]>target):
                r = m -1
            elif(nums[m]<target):
                l = m+1
        else:                   # the last else must be indented outside
                return -1
        
            

        