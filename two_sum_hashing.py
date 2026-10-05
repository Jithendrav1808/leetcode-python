# LeetCode 1 - Two Sum
# Hashing using Dictionary
numbers = [3, 5, 8]
target = 11

seen = {}

for i in range(len(numbers)):

    needed = target - numbers[i]

    if needed in seen:

        print(seen[needed],i)
        break

    seen[numbers[i]] = i

