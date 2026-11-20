class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     
        l,r = 0,1
        maxprofit = 0

        while(r<len(prices)):             #I did while(l<r)
            if prices[r]> prices[l]:
                profit = prices[r]-prices[l]
                maxprofit = max(profit,maxprofit)
                                    # I placed the r+=1 here
            else:
                l=r
            r+=1
        return maxprofit
            





























'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy low and sell high thus we will look for lowest on the left and the highest on the right of it
        l,r = 0,1
        max_profit = 0
        while(r<len(prices)):       
            if prices[l]<prices[r]:
                curr_profit = prices[r]-prices[l]
                max_profit = max(curr_profit,max_profit)
            else:
                l = r
            r+= 1
        return max_profit'''

        