class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_price_past = float('inf')

        for current_price in prices:
            # keep track of the minimum price we've seen in the past
            min_price_past = min(current_price, min_price_past)

            # calculate the profit at this current price
            curr_profit = current_price - min_price_past

            # if the profit we can make now is better, update the max
            max_profit = max(max_profit, curr_profit)

        return max_profit
