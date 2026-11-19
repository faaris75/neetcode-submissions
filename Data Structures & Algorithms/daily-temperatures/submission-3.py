class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_indices = stack.pop()
                output[prev_indices]= i - prev_indices

            stack.append(i)
        return output

                
























# My original solution time limit exceeded because of r checking every single temperature
'''class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l,r = 0,1
        output = []      
        while(l<len(temperatures)):
            if(r>=len(temperatures)):
                output.append(0)
                l+=1
                r=l+1
            elif(temperatures[r]>temperatures[l]):
                output.append(r-l)          
                l+=1
                r=l+1
            else: #This is when temperatures[l]==temperatures[r] or temperatures[r]<temperatures[l]
                r+=1
        return output
'''
       

        