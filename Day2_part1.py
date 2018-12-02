from collections import Counter

f = open("Day2_input.txt", 'r')

x = []

for i in f:
    x.append(i.strip())

count3 = 0
count2 = 0
for i in x:
    a = [j for i, j in Counter(i).most_common()]
    if 2 in a:
        count2 += 1
    if 3 in a:
        count3 += 1
print(count2 * count3)
