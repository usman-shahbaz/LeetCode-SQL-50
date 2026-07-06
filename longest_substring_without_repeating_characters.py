class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        st = set()
        m = 0
        n = len(s)
        l = 0

        for r in range(n):

            while s[r] in st:
                st.remove(s[l])
                l += 1

            st.add(s[r])
            m = max(m, r-l+1)
        return m
