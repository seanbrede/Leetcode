def getPowersOfTwoUpTo(n):
    powers_of_two = []
    x, y = 0, 0
    while y <= n:
        y = 2 ** x
        powers_of_two.append(y)
        x += 1
    powers_of_two.reverse()
    return powers_of_two


def getNextNumber(number, remaining_powers):
    for i in range(len(remaining_powers)):
        if i == -1: print("ERROR!")
        power = remaining_powers[i]
        if power <= number:
            return number - power, remaining_powers[i:]
    return 0, []


def recursiveCount(number, counts, remaining_powers):
    if counts[number] == -1:
        next_number, remaining_powers = getNextNumber(number, remaining_powers)
        counts[number] = recursiveCount(next_number, counts, remaining_powers) + 1
    return counts[number]


class Solution:
    def countBits(self, n: int) -> List[int]:
        # get powers of two in a list up to n
        pwrs_of_two = getPowersOfTwoUpTo(n)

        # initialize return array
        counts = [0] + ([-1] * n)

        # do stuff
        for number in range(n + 1):
            recursiveCount(number, counts, pwrs_of_two)

        return counts
