def longest_increasing_subsequence(arr):
    n = len(arr)
    arr_sorted = sorted(set(arr))
    m = len(arr_sorted)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] == arr_sorted[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[n][m]

# Example usage:
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print(longest_increasing_subsequence(arr))  # Output: 5