#Variable-Size Sliding Window — Minimum Size Subarray Sum

numbers = [2, 3, 1, 2, 4, 3]
target = 7

start = 0
end = 0
win_sum=0
min_len = float("inf")

while end < len(numbers):

    win_sum += numbers[end]
    end +=1

    while win_sum >= target:

        length = end - start

        if length < min_len:
            min_len = length

        win_sum -= numbers[start]
        start += 1

print("minimum_length :",min_len)