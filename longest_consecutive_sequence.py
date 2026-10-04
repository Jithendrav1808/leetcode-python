# LeetCode 128 - Longest Consecutive Sequence
numbers = [100, 4, 200, 1, 3, 2]

numbers_set = set(numbers)

longest = 0

for num in numbers_set:

    if num -1 not in numbers_set:

        current_num = num
        current_length = 1

        while current_num + 1 in numbers_set:
            current_num += 1
            current_length += 1

        if current_length > longest:
            longest = current_length

print("Longest consecutive sequence:", longest)