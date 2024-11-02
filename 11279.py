import sys, heapq

N = int(input())
q = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(q) > 0:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -num)