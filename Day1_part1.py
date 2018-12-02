f = open("Day1_input.txt", 'r')

x = []

for i in f:
    x.append(i.strip())

ans = 0
for i in x:
    ans += int(i)

print(ans)