# LeetCode #125 - Valid Palindrome
# Difficulty: Easy
# Topic: String, Two Pointers
#
# Time Complexity: O(n)
# Space Complexity: O(n)


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:

        # Skip non-alphanumeric characters
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        # Compare characters
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Test Case
s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))