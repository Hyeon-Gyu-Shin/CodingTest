#https://www.acmicpc.net/problem/5397 백준 키로거 5397문제

t = int(input())

for a in range(t):
    right_list = []
    left_list = []
    data = input()
    for i in data:
        if i == '-':
            if left_list:
                left_list.pop()
        elif i == '<':
             if left_list:
                 right_list.append(left_list.pop())
        elif i == '>':
             if right_list:
                 left_list.append(right_list.pop())
        else:
            left_list.append(i)
    left_list.extend(reversed(right_list))
    print(''.join(left_list))
                 
         
        