class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        profit = 0
        max_profit = 0

        for stock_price in prices:
            if stock_price < min_price:
                min_price = stock_price
            profit = stock_price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    assert(Solution().maxProfit(prices) == 5)
    prices = [7,6,4,3,1]
    assert(Solution().maxProfit(prices) == 0)
