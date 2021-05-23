class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        curr_end, count = float('-inf'), 0

        # sort intervals by end time
        intervals.sort(key=lambda x: x[1])

        # for each of the sorted intervals:
        for start, end in intervals:
            # if they don't overlap, use it
            if start >= curr_end:
                curr_end = end
            # otherwise, that's one we can get rid of
            else:
                count += 1

        return count