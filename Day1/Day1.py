input = open("Day1/input_day1.txt").readlines()

# input = [199,
# 200,
# 208,
# 210,
# 200,
# 207,
# 240,
# 269,
# 260,
# 263]

count = 0

for i,j,k,l in zip(input, input[1::], input[2::], input[3::]):
    window1 = int(i) + int(j) + int(k)
    window2 = int(l) + int(j) + int(k)
    if window2 > window1:
        count=count+1 
        
print(count)