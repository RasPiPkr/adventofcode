#! /usr/bin/python3

with open('day03', 'r') as file:
    data = file.read().split()

print('Working data length:', len(data))

joltage = 0

for i in data:
    nums = list(i)
    n = 0
    for ii in range(13, 1, -1):
        if len(nums) >= 1:
            temp = nums[:len(nums) - ii + 2]
        else:
            temp = nums
        num_max = max(temp)
        num_index = temp.index(num_max)
        nums = nums[num_index + 1:]
        n = n * 10 + int(num_max)
    joltage += n

print('Joltage:', joltage)
