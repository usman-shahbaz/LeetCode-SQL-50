def minWindow(s, t):

    tc = Counter(t)
    w = Counter()
    need = len(tc)
    have = 0
    n = len(s)
    l = 0
    ml = float('inf')
    res = [-1, -1]

    if len(t) > len(s):
        return ""
    
    for r in range(n):

        ch = s[r]
        w[ch] += 1

        if ch in tc and tc[ch] == w[ch]:
            have += 1

        while have == need:
            window = r-l+1

            if window < ml:
                ml = window
                res = [l, r]
            
            lef_ch = s[l]
            w[lef_ch] -= 1

            if lef_ch in tc and tc[lef_ch] > w[lef_ch]:
                have -= 1
            l += 1
    l, r = res
    return "" if ml == inf else s[l:r+1]
