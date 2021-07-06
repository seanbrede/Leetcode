class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1]

        if n in range(0, 3):
            return trib[n]

        else:
            trib = trib + ([0] * (n - 2))
            for i in range(3, n + 1):
                trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]

        return trib[n]
