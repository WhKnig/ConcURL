abc = '0123456789ABCDEF'
def hex(x):
    s = ""
    while (x // 8 > 0):
        s += abc[x%8]
        x //= 8
    s += abc[x%8]
    if "3" in s:
        return 1
    else:
        return 0

am = 0
last = 0
f = open("text.txt", 'r')
prev = 7485
max133 = 0
a = []
for line in f.readlines():
    cur = int(line)
    if prev > max133 or cur > max133:
        if hex(prev) or hex(cur):
            a.append([prev, cur])
    if (cur%133 == 0 and cur > max133):
        max133 = cur
    prev = cur

am = 0
mins = 9999999
for i in a:
    if i[0] > max133 or i[1] > max133:
        am += 1
        if (i[0] + i[1] < mins):
            mins = i[0]+i[1]
print(am, mins)