class Solution(object):
    def buy_sell_stock(self, prices: list[int]) -> int:
        max_profit = 0
        L,R = 0,1
        while(R < len(prices)):
            if(prices[R] > prices[L]):
                profit = prices[R] - prices[L]
                max_profit = max(profit, max_profit)
            else: # prices[R] <= prices[L]
                L = R
            R += 1
        return max_profit


# Example:
solution = Solution()
print(solution.buy_sell_stock([7,1,5,3,6,4]))  # Output: 5