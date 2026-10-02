# Variable-Size Sliding Window
# Longest Subarray With Sum <= Target

numbers = [2, 1, 3, 2, 1]
target = 5

start = 0
end = 0
window_sum = 0
max_length = 0

while end < len(numbers):

    # Add the new element
    window_sum += numbers[end]
    end += 1

    # Shrink the window if sum becomes too large
    while window_sum > target:
        window_sum -= numbers[start]
        start += 1

    # Calculate current window length
    length = end - start

    # Keep the largest length
    if length > max_length:
        max_length = length

print("Longest subarray length:", max_length)