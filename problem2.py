D = open("problem2.txt").read().strip()

def is_good(xs):
    incOrDec = (xs==sorted(xs) or xs==sorted(xs, reverse=True))
    ok = True
    for i in range(len(xs) - 1):
        diff = abs(xs[i]-xs[i+1])
        if not 1<=diff<=3:
            ok = False
    return incOrDec and ok

lines = D.split('\n')
p1 = 0
p2 = 0
for line in lines:
    xsl = list(map(int, line.split()))
    if is_good(xsl):
        p1 += 1

    good = False
    for j in range(len(xsl)):
        xs = xsl[:j] + xsl[j+1:]
        if is_good(xs):
            good = True
    if good:
        p2 += 1

print(p1)
print(p2)