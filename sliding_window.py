# Maximum Sum of K Consecutive Elements

numbers = [2, 4, 1, 6, 3]
k = 3

start = 0
end = k

win_sum = 0

for i in range(start,end):
    win_sum += numbers[i]

max_sum = win_sum

while end < len(numbers):

    win_sum = win_sum - numbers[start] + numbers[end]

    if win_sum > max_sum:
        max_sum = win_sum

    start += 1
    end += 1

print("maximum sum : ", max_sum)