num = (1, 1, 2, 2, 2, 8)
chess = input().split()

for i in range(len(num)):
    if chess[i] != num[i] : print(int(num[i])-int(chess[i]), end=" ")
    else: print(0, end = " ")