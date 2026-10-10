
numbers = [1, 1, 1, 2, 2, 3]
k = 2

# Step 1: Count the frequency of each number
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Step 2: Sort by frequency, highest first
sorted_items = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

# Step 3: Extract the first k numbers
result = []

for item in sorted_items[:k]:
    result.append(item[0])

# Step 4: Print the answer
print(result)
