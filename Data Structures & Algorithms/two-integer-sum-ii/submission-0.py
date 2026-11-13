class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while(l<r):
            current_sum = numbers[l] + numbers[r]
            if (current_sum == target):
                return [l+1,r+1]
            elif (current_sum < target):
                l+= 1
            else:
                r-= 1

# The top one is a better solution since it checks from the extreme left and right the bottom one which is my original solution only checks adjacent values. This way if the target was 4 and the array was [1,2,3,4,5] my bottom solution would fail but the top solution works 







'''class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,1
        n = len(numbers)-1
        while(l<n):
            complement = target - numbers[l]
            if(complement == numbers[r]):
                return [l+1,r+1]
            l+=1
            r+=1
'''
        