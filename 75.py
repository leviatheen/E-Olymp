s = input().split()
a = int(s[0])
m = int(s[1])
n = 0


while (m - 2 * a != 0):
    m = m - a
    a += 1
    n += 1

print(n+1)