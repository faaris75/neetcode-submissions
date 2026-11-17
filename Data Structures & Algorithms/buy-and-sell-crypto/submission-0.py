class Solution:
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
        return max_profit

        