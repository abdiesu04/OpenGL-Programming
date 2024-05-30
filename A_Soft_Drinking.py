n, k, l, c, d, p, nl, np = map(int, input().split())

drink = k * l
lime = c * d
salt = p

dp = nl
lp = 1
sp = np

mxdrink = drink // dp
mxlime = lime // lp
mxsalt = salt // sp

res = min(mxdrink, mxlime, mxsalt) // n

print(res)