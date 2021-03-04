""""
Dynamic Programming (DP)

다이나믹 프로그래밍 이란??

특정 범위까지의 값을 구하기 위해 그것과 다른 범위까지의 값을 이용해 효율적으로 값을 구하는 알고리즘입니다.
쉽게말하면 큰 문제를 작은 문제로 나누어 푸는 알고리즘으로
작은 문제의 답을 재활용하는 방식입니다.
엄밀히 말해 동적 계획법은 구체적인 알고리즘 이라기 보다는 문제해결 패러다임에 가깝습니다.

다이나믹 프로그래밍의 조건으로는
1. 작은문제가 반복해서 일어나는 경우
2. 같은 문제는 구할때 마다 정답이 같은 경우

DP의 대표 예시로는 피보나치 수열이 있습니다.
"""

dp = [0 for _ in range(100)] # 리스트 초기화.

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if dp[x] != 0: # 이미 계산한적이 있다면 그대로 반환.
        return dp[x]

    return fibo(x-1) + fibo(x-2)