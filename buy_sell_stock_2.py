def maxProfit(prices):
        p = 0
        n = len(prices) 

        for i in range(n - 1):

            if prices[i] < prices[i+1]:

                p += prices[i+1] - prices[i]

        return p
