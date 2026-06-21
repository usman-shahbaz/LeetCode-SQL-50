def maxProfit(prices):
    
    minprice = float('inf')
    profit = 0

    for price in prices:
        if price < minprice:
            minprice = price
        
        p = price - minprice
        profit = max(profit, p)

    return profit
