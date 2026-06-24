def isSubsequence(s, t):
    m = len(s)
    n = len(t)

    if m == 0: return True
    if m > n: return False
    l = 0

    for ch in t:
        if l < len(s) and s[l] == ch:
            l += 1

    return l == len(s)
