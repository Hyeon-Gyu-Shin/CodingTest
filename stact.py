#백준 1874문제 스택수열 https://www.acmicpc.net/problem/1874

n = int(input())

count = 1
stack = []
result = []
flag = 0

for i in range(n):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        flag = 1
        break
if flag == 0:      
     print('\n'.join(result))
        
        
    