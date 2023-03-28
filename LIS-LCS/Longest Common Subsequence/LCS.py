def lcs(X, Y):
    """
    Returns the length and the actual longest common subsequence of two input sequences.
    """
    m = len(X)
    n = len(Y)
    # Creating a table to store the lengths of the longest common subsequence of prefixes.
    L = [[0] * (n+1) for i in range(m+1)]
    
    # Populating the table in bottom-up fashion.
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    # Finding the length of the longest common subsequence.
    lcs_length = L[m][n]
    
    # Finding the actual longest common subsequence using the table.
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs = X[i-1] + lcs
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return lcs_length, lcs

# Getting input sequences from the user.
X = input("Enter the first sequence: ")
Y = input("Enter the second sequence: ")

# Finding the longest common subsequence and printing it.
lcs_length, lcs = lcs(X, Y)
print(f"The length of the longest common subsequence is {lcs_length}.")
print(f"The longest common subsequence is {lcs}.")