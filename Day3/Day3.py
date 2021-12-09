import functools as ft
input = open("Day3/input_day3.txt").readlines()
# input = [
# "00100",
# "11110",
# "10110",
# "10111",
# "10101",
# "01111",
# "00111",
# "11100",
# "10000",
# "11001",
# "00010",
# "01010",
# ]

def to_digits(string):
    return map(int, string)

def to_number(digits):
    bin_string = ''.join(str(d) for d in digits)
    return int(bin_string, 2)

counts = [0] * (len(input[0])-1)
for i in input:
    for n, digit in enumerate(i.strip()):
        counts[n] += int(digit)

gamma = [(1 if c > len(input)/2 else 0) for c in counts]
epsilon = [1 - g for g in gamma]

print('part 1: ', to_number(gamma) * to_number(epsilon))
