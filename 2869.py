import math

A, B, V = input().split()
x = (int(V) - int(B)) / (int(A) - int(B))
print(math.ceil(x))