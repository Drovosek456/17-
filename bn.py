def dis(a, b, c):
    return b**2 - 4*a*c

def solve(a, b, c):
    return -b / (2*a)

f = open('17_111.txt')
a = [int(x) for x in f]
res = []
for i in range(len(a)-2):
    if dis(a[i], a[i+1], a[i+2]) > 0 and a[i] != 0:
        res.append(solve(a[i], a[i+1], a[i+2]))

print(len(res), int(max(res)))