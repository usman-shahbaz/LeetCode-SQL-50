class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s):
            return False

        need = Counter(t)
        w = Counter()
        l = 0
        n = len(s)

        for r in range(n):
            w[s[r]] += 1

            if r-l+1 > len(s):
                w[s[l]] -= 1
                if w[s[l]] == 0:
                    del w[s[l]]
                l += 1

            if w == need:
                return True
        return False
