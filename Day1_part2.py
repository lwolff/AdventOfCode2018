f = open("Day1_input.txt", 'r')

x = []

for i in f:
    x.append(i.strip())

num = 0
sums = {num}
flag = False
while not flag:
    for i in x:
        num += int(i)
        if num in sums:
            flag = True
            print(num)
            break
        else:
            sums.add(num)
