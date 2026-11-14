class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newnum = sorted(nums)
        res = []
        # i + j + k = 0
        # i = -(j+k)
        #-i = (j+k)
        for i,num in enumerate(newnum):
            if i>0 and num == newnum[i-1]:          # i initially wrote num[i] == newnum[i-1] 
                continue
            target = -num
            l,r = i+1,len(newnum)-1
            while(l<r):
                if(newnum[l]+newnum[r]==target):
                    res.append([newnum[i],newnum[l],newnum[r]])
                    l+=1
                    r-=1               # I did r+= 1 which is wrong
                    while(l<r) and newnum[l] == newnum[l-1]:# Checks for inner 2 pointer duplicates
                        l+=1
                elif((newnum[l]+newnum[r])<target):
                    l+= 1
                else:
                    r-= 1
        return res



        '''
        class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        newnum = sorted(nums)
        l = []
        # i + j + k = 0
        # i = -(j+k)
        #-i = (j+k)
        for i,num in enumerate(newnum):
            if num == newnum[i+1]:          this is wrong as it will go out of bounds when checking for duplicates at the end 


                continue
            target = -num
            l,r = i+1,len(newnum)-1
            while(l<r):
                if(newnum[l]+newnum[r]==target):
                    l.append(newnum[i],newnum[l],newnum[r])
                    l+=1
                    r+=1    
                elif((newnum[l]+newnum[r])<target):
                    l+= 1
                else:
                    r-= 1

        '''

        