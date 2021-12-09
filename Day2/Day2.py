input = open("Day2/input_day2.txt").readlines()
# input = ["forward 5",
# "down 5",
# "forward 8",
# "up 3",
# "down 8",
# "forward 2"]

horizontal = 0
depth = 0
aim=0

for i in input:
    command, magnitude_string = i.split()
    magnitude = int(magnitude_string)
    if command == "forward":
        horizontal = horizontal+magnitude
        depth = depth + (magnitude*aim)
    if command == "down":
        aim = aim + magnitude
    if command == "up":
        aim = aim - magnitude
        
print(horizontal)
print(depth)
print(horizontal*depth)