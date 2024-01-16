#https://www.acmicpc.net/problem/1655 백준 1655 가운데로 말해요

'''
n = int(input())
t = []
answer = []

for i in range(n):
    t.append(int(input()))
    # 입력을 모두 받은 후에 정렬
    t.sort()

    # 중앙값의 인덱스 계산
    mid = len(t)//2
    check = len(t)%2
    if check == 0:
        answer.append(t[mid-1])
    else:
        answer.append(t[mid])

for a in range(n):
    print(answer[a])

#시간 초과로 인한 폐기 
#아 뭔 문제를 일케 내
'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())
left_heap = []   # 최대 힙
right_heap = []  # 최소 힙

for _ in range(n):
    x = int(input())

    # 최대 힙과 최소 힙에 번갈아가며 삽입
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -x)
    else:
        heapq.heappush(right_heap, x)

    # 최대 힙의 최댓값이 최소 힙의 최솟값보다 크다면 교환
    if left_heap and right_heap and left_heap[0] * -1 > right_heap[0]:
        max_value = heapq.heappop(left_heap)
        min_value = heapq.heappop(right_heap)

        # 교환 후 다시 최대 힙과 최소 힙에 삽입
        heapq.heappush(left_heap, min_value * -1)
        heapq.heappush(right_heap, max_value * -1)

    # 현재 중앙값 출력 (최대 힙의 최댓값이 중앙값)
    print(left_heap[0] * -1)
