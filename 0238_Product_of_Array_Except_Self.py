class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get product of all nonzero numbers, and the number of zeroes
        product = 1
        num_zeroes = 0
        for n in nums:
            if n == 0: num_zeroes += 1
            else:      product *= n

        # if there's more than 1 zero, all numbers are zero
        if num_zeroes > 1:
            return [0] * len(nums)

        # otherwise, iterate over all numbers with 2 cases
        else:
            answer = []
            for n in nums:
                # if there are no zeroes, the answer at this place is
                # the total product divided by that number
                if num_zeroes == 0:
                    answer.append(product // n)

                # if there is one zero:
                elif num_zeroes == 1:
                    # then the answer at that zero is the product of all nonzero numbers
                    if n == 0:
                        answer.append(product)
                    # and the answer at every other place is zero
                    else:
                        answer.append(0)

            return answer
