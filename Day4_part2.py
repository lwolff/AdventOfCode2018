f = open("Day4_input.txt", 'r')

x = []

for i in f:
    x.append(i.strip())
x.sort()

guard = "null"
asleep = [0 for x in range(60)]
timeAsleep = -1
chart = {}
for i in x:
    time = int(i.split()[1][3:5])
    if "Guard" in i:
        if guard != "null":
            chart.update({guard: asleep})
        guard = i.split()[3][1:]
        if guard in chart:
            asleep = chart[guard]
        else:
            asleep = [0 for x in range(60)]

    elif "falls asleep" in i:
        timeAsleep = time
    elif "wakes up" in i:
        for j in range(timeAsleep, time):
            asleep[j] += 1

chart.update({guard: asleep})
maxSlept = 0
maxGuard = 0
for i in chart:
    if max(chart[i]) > maxSlept:
        maxSlept = max(chart[i])
        maxGuard = i
maxTime = -1
minute = -1
count = 0
for i in chart[maxGuard]:
    if i > maxTime:
        maxTime = i
        minute = count
    count += 1
print(minute * int(maxGuard))
