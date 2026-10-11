
# product_except_self.py

numbers = [1, 2, 3, 4]

# Step 1: Prefix products
prefix = []
product = 1

for num in numbers:
    prefix.append(product)
    product *= num

# Step 2: Suffix products
suffix = [1] * len(numbers)
product = 1

for i in range(len(numbers) - 1, -1, -1):
    suffix[i] = product
    product *= numbers[i]

# Step 3: Calculate the result
result = []

for i in range(len(numbers)):
    result.append(prefix[i] * suffix[i])

print(result)
