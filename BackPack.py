#백준 평범한 배낭 12865문제 https://www.acmicpc.net/problem/12865
import sys

# 입력 받기
N, K = map(int, input().split())
stuff = [[0, 0]]  # 물건의 정보를 담는 리스트, 인덱스 0은 사용하지 않음
knapsack = [[0] * (K + 1) for _ in range(N + 1)]  # 냅색 테이블 초기화

# 각 물건의 정보 입력 받기
for _ in range(N):
    stuff.append(list(map(int, input().split())))

# 냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]  # 현재 물건의 무게
        value = stuff[i][1]   # 현재 물건의 가치

        if j < weight:
            # 현재 물건을 배낭에 넣을 수 없는 경우, 위의 값을 그대로 가져옴
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            # 현재 물건을 배낭에 넣을 수 있는 경우,
            # 현재 물건을 넣지 않은 경우와 넣은 경우 중 더 큰 가치 선택
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

# 결과 출력
print(knapsack[N][K])
