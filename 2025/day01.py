#! /usr/bin/python3

dial = 50
rotation = ''
zeros = 0

with open('day01', 'r') as file:
    data = file.read().split()

print('Working data:', len(data))

for i in data:
    rotation = i[0]
    moves = int(i[1:]) + 1
    for turns in range(1, moves):
        if rotation == 'L':
            dial -= 1
        else:
            dial += 1
        if dial == -100:
            zeros += 1
            dial =0
        elif dial == 0:
            zeros += 1
        elif dial == 100:
            zeros += 1
            dial = 0

print('Total times:', zeros)
