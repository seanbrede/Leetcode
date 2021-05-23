class Solution:
    def climbStairs(self, n: int) -> int:
        # intialize the array to hold the values
        counts = [0, 1, 2]
        if n > 2: counts += [-1] * (n - 2)

        ways = stepCount(n, counts)

        return ways


def stepCount(n, counts):
    # if the answer for this n doesn't exist in the array of counts, build it
    if counts[n] == -1:
        counts[n] = stepCount(n - 1, counts) + stepCount(n - 2, counts)

    return counts[n]
