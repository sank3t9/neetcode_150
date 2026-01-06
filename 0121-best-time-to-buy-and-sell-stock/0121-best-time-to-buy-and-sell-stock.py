class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        n = len(prices)
        # min_price = float("inf")
        cost_price = prices[0]

        for i in range(1, n):
            sell_price = prices[i]
            profit = sell_price - cost_price

            if profit > max_profit:
                max_profit = profit

            if cost_price > prices[i]:
                cost_price = prices[i]


        return max_profit


        