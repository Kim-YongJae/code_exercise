import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = list(map(int, input().split()))
S.sort()

i = 0
j = N-1
count = 0

while i < j:
    if S[i] + S[j] > M:
        j-=1
    elif S[i] + S[j] < M:
        i+=1
    else:
        count+=1
        i+=1
        j-=1

print(count)