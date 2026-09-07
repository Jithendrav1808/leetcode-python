# LeetCode #121 - Best Time to Buy and Sell Stock
# Difficulty: Easy
# Topic: Array, Greedy
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


# Test Case
prices = [7, 1, 5, 3, 6, 4]

print(max_profit(prices))