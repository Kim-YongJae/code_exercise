import sys

A=[0]*4
B=[0]*4
C=0

def add(x):
    global A, B, C
    if x=='A':
        B[0]+=1
        if A[0]==B[0]:
            C+=1
    elif x=='C':
        B[1]+=1
        if A[1]==B[1]:
            C+=1
    elif x=='G':
        B[2]+=1
        if A[2]==B[2]:
            C+=1
    elif x=='T':
        B[3]+=1
        if A[3]==B[3]:
            C+=1

def sub(x):
    global A, B, C
    if x=='A':
        if A[0]==B[0]:
            C-=1
        B[0]-=1
    elif x=='C':
        if A[1]==B[1]:
            C-=1
        B[1]-=1
    elif x=='G':
        if A[2]==B[2]:
            C-=1
        B[2]-=1
    elif x=='T':
        if A[3]==B[3]:
            C-=1
        B[3]-=1

input = sys.stdin.readline
N, M = map(int,input().split())
S=list(input())
A=list(map(int,input().split()))
result=0

for i in range(4):
    if A[i]==0:
        C+=1

for i in range(M):
    add(S[i])

if C==4:
    result+=1

for i in range(M,N):
    j=i-M
    add(S[i])
    sub(S[j])
    if C==4:
        result+=1

print(result)