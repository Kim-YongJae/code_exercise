N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

B = []
number=1
result=True
answer=""

for i in range(N):
    if A[i]>=number:
        while A[i]>=number:
            B.append(number)
            number+=1
            answer+='+\n'
        B.pop()
        answer+='-\n'
    else:
        n=B.pop()
        if n>A[i]:
            print('NO')
            result=False
            break
        else:
            answer+='-\n'

if result:
    print(answer)