from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    # intervals are NON-OVERLAPPING
    # intervals are sorted in ascending order (by start number)
    # intervals[i-1][1] < intervals[i][0] < intervals[i][1] < intervalse[i+1][0]

    # goal is to insert a new interval so that intervals array is still sorted in asc order
    # new interval may overlap with pre-existing intervals
    # if so, the intervals must be MERGED so that there is no overlap
    # finally, return updated intervals array (in place!)

    # base case (can probably exclude at some point)
    if not intervals:
        intervals.append(newInterval)
        return intervals

    lo = 0
    hi = len(intervals) - 1

    while lo <= hi:
        mid = lo + (hi - lo + 1) // 2

        # if new interval start > mid interval end
        # and new end < mid+1 start, insert and return
        # else repeat with right half of array
        if newInterval[0] > intervals[mid][1]:
            if mid+1 < len(intervals):
                if newInterval[1] < intervals[mid+1][0]:
                    intervals.insert(mid+1, newInterval)
                    return intervals
                else:
                    lo = mid + 1
            else:
                intervals.append(newInterval)
                return intervals

        # if new interval end < mid interval start, 
        # and new start > mid-1 end, insert and return
        # else repeat with left half of array
        elif newInterval[1] < intervals[mid][0]:
            if mid-1 >= 0:
                if newInterval[0] > intervals[mid-1][1]:
                    intervals.insert(mid, newInterval)
                    return intervals
                else:
                    hi = mid - 1
            else:
                intervals.insert(0, newInterval)
                return intervals

        # if we get here, we know there is some overlap
        # if new start >= mid start, we already have our insertion index at mid
        elif newInterval[0] >= intervals[mid][0]:
            # update new interval start to be min of prev start or mid start
            newInterval[0] = min(newInterval[0], intervals[mid][0])
            # update new interval end to max of new end vs overlapping ends
            hi = mid
            while hi+1 < len(intervals) and newInterval[1] >= intervals[hi+1][0]:
                hi += 1
            newInterval[1] = max(newInterval[1], intervals[hi][1])
            # insert the new interval at relevant index
            intervals.insert(mid, newInterval)
            # delete all overlapping intervals and return
            for i in range(mid+1, hi+2):
                del intervals[mid + 1]
            return intervals

        # reverse logic if new end <= mid end
        elif newInterval[1] <= intervals[mid][1]:
            newInterval[1] = max(newInterval[1], intervals[mid][1])
            lo = mid
            while lo - 1 >= 0 and newInterval[0] <= intervals[lo-1][1]:
                lo -= 1
            newInterval[0] = min(newInterval[0], intervals[lo][0])
            intervals.insert(mid, newInterval)
            del intervals[mid+1]
            for i in range(lo, mid):
                del intervals[lo]
            return intervals

        # if new interval overlaps and extends past mid
        elif newInterval[0] < intervals[mid][0] or newInterval[1] > intervals[mid][1]:
            lo = hi = mid
            while lo - 1 >= 0 and newInterval[0] <= intervals[lo-1][1]:
                lo -= 1
            newInterval[0] = min(newInterval[0], intervals[lo][0])
            while hi+1 < len(intervals) and newInterval[1] >= intervals[hi+1][0]:
                hi += 1
            newInterval[1] = max(newInterval[1], intervals[hi][1])
            intervals.insert(mid, newInterval)
            for i in range(mid+1, hi+2):
                del intervals[mid + 1]
            for i in range(lo, mid):
                del intervals[lo]

            return intervals

insert([[1,5],[6,8]], [5,6])