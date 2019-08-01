"""
Max Profit With K Transactions

You are given an array of integers representing the prices of a single stock on various
days (each index in the array represents a different day). You are also given an integer
k, which represents the number of transactions you are allowed to make. One transaction
consists of buying the stock on a given day and selling it on another, later day. Write
a function that returns the maximum profit that you can make buying and selling the
stock, given k transactions. Note that you can only hold 1 share of the stock at a time;
in other words, you cannot buy more than 1 share of the stock on any given day, and you
cannot buy a share of the stock if you are still holding another share.

Sample input: [5, 11, 3, 50, 60, 90], 2
Sample output: 93
Explanation: Buy: 5, Sell: 11; Buy: 3, Sell: 90
"""


def max_profit_with_k_transactions(prices: list, k: int) -> int:
    if not prices:
        return 0

    profits = [[0 for _ in prices] for __ in range(k + 1)]

    for t in range(1, k + 1):
        max_throw_far = float('-inf')
        for d in range(1, len(prices)):
            max_throw_far = max(max_throw_far, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d - 1], prices[d] + max_throw_far)

    return profits[-1][-1]


prices = [5, 11, 3, 50, 60, 90]
k = 2
result = max_profit_with_k_transactions(prices=prices, k=k)
print(result)
