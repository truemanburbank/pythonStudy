numbers = [list(map(int, input().split())) for _ in range(5)]
score =[]
for i in range(5):
    score.append(sum(numbers[i]))
print(score.index(max(score)) + 1, max(score))
