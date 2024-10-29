import sys

N, K = map(int, sys.stdin.readline().split())
number = sys.stdin.readline().strip()
stack = []
for i in range(N):
    while K > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        K -= 1
    stack.append(number[i])
print(''.join(stack[:len(stack)-K]))
