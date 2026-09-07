# LeetCode #1 - Two Sum
# Difficulty: Easy
# Topic: Array, Hash Map
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i


# Test
nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))