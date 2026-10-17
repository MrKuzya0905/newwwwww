def min_cost(N):
    dp = [0] * (N + 1)

    for i in range(1, N + 1):
        dp[i] = dp[i - 1] + 2

        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 5)

        if i >= 7:
            dp[i] = min(dp[i], dp[i - 7] + 10)

    return dp[N]


N = int(input("Введіть кількість днів: "))
print("Мінімальна вартість:", min_cost(N), "грн")