import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum=[0]
hap=0

for i in numbers:
    hap+=i
    sum.append(hap)

for a in range(M):
    i, j = map(int, input().split())
    print(sum[j]-sum[i-1])