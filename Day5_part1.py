f = open("Day5_input.txt", 'r')

x = ""

for i in f:
    x = i.strip()

ans = [""]
for i in x:
    if i.swapcase() == ans[-1]:
        ans.pop()
    else:
        ans.append(i)
print(str(len(ans) - 1))
