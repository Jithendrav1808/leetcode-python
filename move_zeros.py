# LeetCode #283 - Move Zeroes
# Difficulty: Easy
# Topic: Array, Two Pointers
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def move_zeroes(nums):
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1


# Test Case
nums = [0, 1, 0, 3, 12]

move_zeroes(nums)

print(nums)