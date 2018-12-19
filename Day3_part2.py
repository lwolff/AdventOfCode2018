import re

f = open("Day3_input.txt", 'r')

x = []

for i in f:
    x.append(re.findall('\d+', i))

w = 0
h = 0
for i in x:
    if (int(i[1]) + int(i[3])) > w:
        w = (int(i[1]) + int(i[3]))
    if (int(i[2]) + int(i[4])) > h:
        h = (int(i[2]) + int(i[4]))

fabric = [[0 for x in range(w + 1)] for y in range(h + 1)]

for i in x:
    for j in range(int(i[3])):
        for k in range(int(i[4])):
            fabric[int(i[1]) + j - 1][int(i[2]) + k - 1] += 1

ans = 0

for i in x:
    win = True
    for j in range(int(i[3])):
        for k in range(int(i[4])):
            if fabric[int(i[1]) + j - 1][int(i[2]) + k - 1] != 1:
                win = False
    if win:
        print(int(i[0]))
        break
