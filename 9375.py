N = int(input())

for i in range(N):
    clothes = int(input())
    comb = {}
    ans = 1
    for j in range(clothes):
        name, type = input().split()
        if not type in comb:
            comb[type] = 1
        else:
            comb[type] += 1

    for key in comb.keys():
        ans *= (comb[key] + 1)
    print(ans - 1)