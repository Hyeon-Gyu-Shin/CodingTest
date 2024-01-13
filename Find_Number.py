#백준 1920문제 https://www.acmicpc.net/problem/1920

n = int(input())
array = set(map(int, input().split())) #set은 중복을 받지 않는다
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in array:
        print('0')
    else:
        print('1')
