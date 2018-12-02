from difflib import get_close_matches

f = open("Day2_input.txt", 'r')

x = []

for i in f:
    x.append(i.strip())
#match 25 of 26 chars
for i in x:
    n = get_close_matches(i, x, cutoff=(25/26))
    if len(n) > 1:
        ans = ""
        for a, b in zip(n[0], n[1]):
            if a == b:
                ans += a
        print(ans)
        break

