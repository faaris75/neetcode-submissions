class Solution:
    def maxArea(self, heights: List[int]) -> int:
        list = []
        l,r = 0, len(heights)-1
        while(l<r):
            width = r-l
            height = min(heights[l],heights[r])
            area = width*height
            list.append(area)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        maxarea = max(list)
        return maxarea




























'''class Solution:
    def maxArea(self, heights: List[int]) -> int:
        heights.sort()
        for i in range(len(heights)):
            r1 = len(heights)-1
            r2 = len(heights)-2
            if(heights[r1]!=heights[r2]):
                width = heights[r1]-heights[r2]
                height = heights[r2]
                maxarea = height*width
            else:
                maxarea = heights[r1]*heights[r2]
        return maxarea
'''          
