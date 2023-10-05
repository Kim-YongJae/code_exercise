from collections import deque

N, L = map(int,input().split())
deque1 = deque()
now = list(map(int,input().split()))

for i in range(N):
    while deque1 and deque1[-1][0] > now[i]:
        deque1.pop()
    deque1.append((now[i],i))
    if deque1[0][1] <= i-L:
        deque1.popleft()
    print(deque1[0][0], end=' ')