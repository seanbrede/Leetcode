class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use a hash set to detect duplicates efficiently
        detect_dupes = set()

        # for each number:
        for n in nums:
            # if it's already in the set, there's a duplicate
            if n in detect_dupes:
                return True
            # otherwise, add it
            else:
                detect_dupes.add(n)

        # if we get here, there were no duplicates
        return False
