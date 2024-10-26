entirePrice = int(input())
entireNum = int(input())

add = 0

for i in range(entireNum):
    price, num = input().split()
    add += int(price) * int(num)

if add == entirePrice: print("Yes")
else : print("No")