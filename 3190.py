from collections import deque

N = int(input())
board  = [[0] * N for _ in range(N)]

K = int(input())
for i in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

Ls = deque()
L = int(input())
for i in range(L):
    time, direction = input().split()
    Ls.append((int(time), direction))

# 상우하좌
dirY = [-1, 0, 1, 0]
dirX = [0, 1, 0, -1]

snake = deque()
snake.append((0, 0))

# index
curDir = 1

time = 0
while True:
    if Ls and Ls[0][0] == time:
        if Ls[0][1] == 'L':
            curDir = (curDir - 1) % 4
        else:
            curDir = (curDir + 1) % 4
        Ls.popleft()
    nextY = snake[-1][0] + dirY[curDir]
    nextX = snake[-1][1] + dirX[curDir]

    time += 1

    if 0 <= nextY < N and 0 <= nextX < N and board[nextY][nextX] != 2:
        snake.append((nextY, nextX))
        tailY = snake[0][0]
        tailX = snake[0][1]
        if board[nextY][nextX] == 1:
            board[tailY][tailX] = 2
        else:
            snake.popleft()
            board[tailY][tailX] = 0
        board[nextY][nextX] = 2
    else:
        break

print(time)