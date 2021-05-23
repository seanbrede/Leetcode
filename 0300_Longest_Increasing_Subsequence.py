class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp array; Lowest ending Number for each SubSequence Length
        ln_for_ssl = []

        for num in nums:
            # use binary search to find this number's position
            ind = bisect_left(ln_for_ssl, num)

            # either the num makes a new longest subsequence
            if ind == len(ln_for_ssl):
                ln_for_ssl.append(num)

            # or it's at least as good an ending number for some existing subsequence
            else:
                ln_for_ssl[ind] = num

        # the dp array isn't the actual subsequence but its length is the answer
        return len(ln_for_ssl)
