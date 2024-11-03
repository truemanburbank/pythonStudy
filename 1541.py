# 첫 숫자는 무조건 양수이고, < 얘가 문제
# 마이너스 부호가 나왔을 때 다음 마이너스가 나오기 전까지
# 최대한 괄호를 넓게 쳐서 다 빼버린다.
# 그럼 최솟값 아닐까?
a = input()
case = list(a)
flag = False
for i in range(len(case)):
    if case[i] == "-":
        flag = True
    elif case[i] == "+":
        if flag is True:
            case[i] = "-"

num = []
n = ""
for i in range(len(case)):
    if case[i] == "+" or case[i] == "-":
        num.append(str(int(n)))
        n = ""
        num.append(case[i])
    else:
        n += case[i]
num.append(str(int(n)))
print(eval(("".join(num))))


