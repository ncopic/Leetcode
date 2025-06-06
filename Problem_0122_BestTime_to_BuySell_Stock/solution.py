class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #-------------------------------------------------------------------
        # Solution 1 - Question is really "if next number is bigger, find the difference and tally it"
        #-------------------------------------------------------------------
        profit = 0

        if len(prices) == 1:#if we only have 1 day of data, there is no profit
            return profit

        for ii in range(len(prices)-1):
            if prices[ii] < prices[ii+1]: #if today's prices are lower than tomorrow's
                profit = profit + (prices[ii+1] - prices[ii])
        return profit