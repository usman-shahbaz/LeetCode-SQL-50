class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        c = []
        r = []
        n = len(nums)
        used = [False] * n

        def b():
            if len(c) == n:
                r.append(c[:])

            for i in range(n):

                if used[i]:
                    continue

                c.append(nums[i])
                used[i] = True

                b()

                c.pop()
                used[i] = False

        b()
        return r
