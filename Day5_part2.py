from string import ascii_lowercase
f = open("Day5_input.txt", 'r')

x = ""

for i in f:
    x = i.strip()

minLength = len(x)
for i in ascii_lowercase:
    polymers = [j for j in x if j.lower() != i]
    ans = [""]
    for j in polymers:
        if j.swapcase() == ans[-1]:
            ans.pop()
        else:
            ans.append(j)
    length = len(ans) - 1
    if length < minLength:
        minLength = length
print(str(minLength))
