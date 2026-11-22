"""Comparison-based sorting algorithms.

Every function takes any iterable of comparable items and returns a NEW
sorted list in ascending order. The input is never modified.
Pass ``reverse=True`` to sort in descending order.
"""

from typing import Iterable, List, TypeVar

T = TypeVar("T")


def _finish(items: List[T], reverse: bool) -> List[T]:
    if reverse:
        items.reverse()
    return items


# ---------------------------------------------------------------------------
# O(n^2) algorithms — simple, good for learning and tiny inputs
# ---------------------------------------------------------------------------

def bubble_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Repeatedly swap adjacent items that are out of order.

    Time: best O(n) (already sorted), average/worst O(n^2). Space: O(1). Stable.
    """
    arr = list(data)
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        # After each pass the largest remaining item "bubbles" to the end.
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # no swaps means the list is already sorted
            break
    return _finish(arr, reverse)


def selection_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Find the smallest remaining item and move it to the front.

    Time: O(n^2) in all cases. Space: O(1). Not stable.
    """
    arr = list(data)
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return _finish(arr, reverse)


def insertion_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Grow a sorted prefix by inserting each new item into its place.

    Time: best O(n), average/worst O(n^2). Space: O(1). Stable.
    Very fast on small or nearly sorted lists.
    """
    arr = list(data)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift bigger items one step right to make room for key.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return _finish(arr, reverse)


def shell_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Insertion sort over shrinking gaps, so items move far in one step.

    Time: depends on the gap sequence; about O(n^1.5) with gap halving.
    Space: O(1). Not stable.
    """
    arr = list(data)
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return _finish(arr, reverse)


# ---------------------------------------------------------------------------
# O(n log n) algorithms — what you use for real workloads
# ---------------------------------------------------------------------------

def merge_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Divide the list in half, sort each half, then merge them.

    Time: O(n log n) in all cases. Space: O(n). Stable.
    """
    def _sort(arr: List[T]) -> List[T]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        return _merge(_sort(arr[:mid]), _sort(arr[mid:]))

    def _merge(left: List[T], right: List[T]) -> List[T]:
        merged: List[T] = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # <= keeps equal items in order (stable)
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    return _finish(_sort(list(data)), reverse)


def quick_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Pick a pivot, partition items around it, and sort each side.

    In-place version using Lomuto partitioning with a median-of-three pivot,
    which avoids the O(n^2) worst case on already sorted input.
    Time: average O(n log n), worst O(n^2). Space: O(log n). Not stable.
    """
    arr = list(data)

    def _median_of_three(lo: int, hi: int) -> None:
        mid = (lo + hi) // 2
        if arr[mid] < arr[lo]:
            arr[mid], arr[lo] = arr[lo], arr[mid]
        if arr[hi] < arr[lo]:
            arr[hi], arr[lo] = arr[lo], arr[hi]
        if arr[mid] < arr[hi]:
            arr[mid], arr[hi] = arr[hi], arr[mid]
        # The median now sits at arr[hi] and is used as the pivot.

    def _partition(lo: int, hi: int) -> int:
        _median_of_three(lo, hi)
        pivot = arr[hi]
        i = lo
        for j in range(lo, hi):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        return i

    def _sort(lo: int, hi: int) -> None:
        # Recurse into the smaller side and loop on the larger one,
        # so recursion depth stays O(log n).
        while lo < hi:
            p = _partition(lo, hi)
            if p - lo < hi - p:
                _sort(lo, p - 1)
                lo = p + 1
            else:
                _sort(p + 1, hi)
                hi = p - 1

    _sort(0, len(arr) - 1)
    return _finish(arr, reverse)


def heap_sort(data: Iterable[T], reverse: bool = False) -> List[T]:
    """Build a max-heap, then repeatedly move the largest item to the end.

    Time: O(n log n) in all cases. Space: O(1). Not stable.
    """
    arr = list(data)
    n = len(arr)

    def _sift_down(start: int, end: int) -> None:
        root = start
        while True:
            child = 2 * root + 1
            if child >= end:
                return
            if child + 1 < end and arr[child] < arr[child + 1]:
                child += 1  # pick the larger child
            if arr[root] < arr[child]:
                arr[root], arr[child] = arr[child], arr[root]
                root = child
            else:
                return

    for start in range(n // 2 - 1, -1, -1):  # build the heap
        _sift_down(start, n)
    for end in range(n - 1, 0, -1):          # extract max one by one
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down(0, end)
    return _finish(arr, reverse)
