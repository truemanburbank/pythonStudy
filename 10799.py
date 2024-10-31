import sys
metal = sys.stdin.readline().strip()
ans = 0
stack = []
for i in range(len(metal)):
    if metal[i] == '(':
        stack.append(metal[i])
    else:
        if metal[i - 1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop()
            ans += 1
print(ans)
