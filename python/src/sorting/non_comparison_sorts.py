"""Non-comparison sorting algorithms.

These do not compare items against each other. Instead they use the values
themselves (as counts, digits or buckets), which lets them beat O(n log n)
for the right kind of data.

Every function returns a NEW sorted list; the input is never modified.
"""

from typing import Iterable, List


def counting_sort(data: Iterable[int], reverse: bool = False) -> List[int]:
    """Count how many times each integer appears, then rebuild the list.

    Works with negative integers too (values are offset by the minimum).
    Time: O(n + k), where k is the range (max - min). Space: O(n + k). Stable.
    Best when the range of values is small compared to the number of items.
    """
    arr = list(data)
    if not arr:
        return []
    for x in arr:
        if not isinstance(x, int):
            raise TypeError("counting_sort only supports integers")

    lo, hi = min(arr), max(arr)
    counts = [0] * (hi - lo + 1)
    for x in arr:
        counts[x - lo] += 1

    # Prefix sums tell us the final position of each value (keeps it stable).
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    output = [0] * len(arr)
    for x in reversed(arr):
        counts[x - lo] -= 1
        output[counts[x - lo]] = x

    if reverse:
        output.reverse()
    return output


def radix_sort(data: Iterable[int], reverse: bool = False) -> List[int]:
    """Sort integers digit by digit, from least to most significant (LSD).

    Negative numbers are sorted separately and placed before the positives.
    Time: O(d * (n + b)), d = number of digits, b = base (10). Space: O(n + b).
    Stable.
    """
    arr = list(data)
    for x in arr:
        if not isinstance(x, int):
            raise TypeError("radix_sort only supports integers")

    def _lsd(nums: List[int]) -> List[int]:
        if not nums:
            return nums
        exp = 1
        biggest = max(nums)
        while biggest // exp > 0:
            buckets: List[List[int]] = [[] for _ in range(10)]
            for x in nums:
                buckets[(x // exp) % 10].append(x)
            nums = [x for bucket in buckets for x in bucket]
            exp *= 10
        return nums

    negatives = _lsd([-x for x in arr if x < 0])
    positives = _lsd([x for x in arr if x >= 0])
    result = [-x for x in reversed(negatives)] + positives

    if reverse:
        result.reverse()
    return result


def bucket_sort(data: Iterable[float], reverse: bool = False,
                bucket_count: int = 10) -> List[float]:
    """Spread numbers into evenly sized buckets, sort each, then join them.

    Works for any int/float values (they are scaled to the min..max range).
    Time: average O(n + k) for evenly spread data, worst O(n^2).
    Space: O(n + k). Stable (each bucket uses insertion sort).
    """
    arr = list(data)
    if len(arr) <= 1:
        return arr
    if bucket_count < 1:
        raise ValueError("bucket_count must be at least 1")

    lo, hi = min(arr), max(arr)
    if lo == hi:
        return arr

    width = (hi - lo) / bucket_count
    buckets: List[List[float]] = [[] for _ in range(bucket_count)]
    for x in arr:
        idx = min(int((x - lo) / width), bucket_count - 1)
        buckets[idx].append(x)

    result: List[float] = []
    for bucket in buckets:
        # Insertion sort is fast for the small lists inside each bucket.
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key
        result.extend(bucket)

    if reverse:
        result.reverse()
    return result
