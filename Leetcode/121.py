class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1] - prices[0])
        else:
            low = min(prices[1], prices[0])
            ans = max(0, prices[1] - prices[0])

            for price in prices[2:]:
                a = price - low
                if a > ans:
                    ans = a
                low = min(low, price)
            return ans

