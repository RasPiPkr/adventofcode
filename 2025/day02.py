#! /usr/bin/python3

invalid_id_sum = 0

with open('day02', 'r') as file:
    data = file.read().split()

# Handle the data
data = data[0].split(',')

print('Working data:', len(data))

def pattern_check(num1, num2):
    global invalid_id_sum
    for i in range(int(num1), int(num2) + 1):
        i_str = str(i)
        for ii in range(2, len(i_str) + 1):
            if len(i_str) % ii == 0 and i_str[:len(i_str) // ii] * ii == i_str:
                invalid_id_sum += (int(i_str))
                break

for i in data:
    num1, num2 = i.split('-')
    pattern_check(num1, num2)

print('Invalid id sum:', invalid_id_sum)
