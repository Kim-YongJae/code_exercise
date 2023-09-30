N= input()
scores = list(map(int, input().split()))
max = max(scores)
sum = sum(scores)

print((sum/max*100)/int(N))