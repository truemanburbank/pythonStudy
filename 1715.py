import sys, heapq
n = int(input())
q = []
for i in range(n):
    num = int(sys.stdin.readline().strip())
    heapq.heappush(q, num)
ans = 0
while len(q) > 1:
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    sum = a + b
    ans += sum
    heapq.heappush(q, sum)
print(ans)
