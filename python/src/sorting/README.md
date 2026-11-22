# 🔢 Sorting Techniques in Python

Ten classic sorting algorithms written from scratch in pure Python (no external libraries), with comments, complexity notes, a demo, a benchmark and unit tests.

## 📂 Files

```
src/sorting/
├── __init__.py              # exports every algorithm + ALGORITHMS dict
├── __main__.py              # demo and benchmark (python -m src.sorting)
├── comparison_sorts.py      # bubble, selection, insertion, shell, merge, quick, heap
├── non_comparison_sorts.py  # counting, radix, bucket
└── README.md

tests/test_sorting.py        # pytest tests for every algorithm
```

## 🧠 Algorithms at a glance

| Algorithm | Best | Average | Worst | Extra space | Stable | Idea |
|---|---|---|---|---|---|---|
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | Swap neighbours that are out of order; stop early if no swaps |
| Selection sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ | Pick the smallest remaining item and put it next |
| Insertion sort | O(n) | O(n²) | O(n²) | O(1) | ✅ | Insert each item into its place in a sorted prefix |
| Shell sort | O(n log n) | ~O(n^1.5) | O(n²) | O(1) | ❌ | Insertion sort over shrinking gaps |
| Merge sort | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Split in half, sort each half, merge |
| Quick sort | O(n log n) | O(n log n) | O(n²) | O(log n) | ❌ | Partition around a pivot (median of three), sort each side |
| Heap sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Build a max-heap, pull out the max repeatedly |
| Counting sort | O(n + k) | O(n + k) | O(n + k) | O(n + k) | ✅ | Count each value; k = value range. Integers only |
| Radix sort | O(d·n) | O(d·n) | O(d·n) | O(n) | ✅ | Sort digit by digit (LSD); d = digits. Integers only |
| Bucket sort | O(n + k) | O(n + k) | O(n²) | O(n + k) | ✅ | Spread values into buckets, sort each, join |

## 🧭 Which one should I use?

- **Real projects:** use Python's built-in `sorted()` / `list.sort()` (Timsort, a hybrid of merge and insertion sort). It's written in C and beats all of these.
- **Small or nearly sorted lists:** insertion sort.
- **Guaranteed O(n log n):** merge sort (stable) or heap sort (no extra memory).
- **Fastest on average in practice:** quick sort.
- **Integers in a small range:** counting sort. **Large integers:** radix sort.
- **Evenly spread floats:** bucket sort.
- **Learning only:** bubble and selection sort.

## 🚀 Usage

Every function returns a **new** sorted list (the input is not changed), accepts any iterable, and takes `reverse=True` for descending order.

```python
from src.sorting import quick_sort, merge_sort, counting_sort

quick_sort([5, 2, 9, 1])                  # [1, 2, 5, 9]
merge_sort(["pear", "apple", "fig"])      # ['apple', 'fig', 'pear']
counting_sort([3, -1, 2], reverse=True)   # [3, 2, -1]
```

Or pick an algorithm by name:

```python
from src.sorting import ALGORITHMS

ALGORITHMS["heap"]([4, 1, 3])  # [1, 3, 4]
```

Notes:
- Comparison sorts work with anything comparable (numbers, strings, tuples).
- `counting_sort` and `radix_sort` accept integers only (negatives are fine); they raise `TypeError` otherwise.
- `bucket_sort` works with ints and floats; `bucket_count` is optional (default 10).

## ▶️ Demo and benchmark

Run from the repository root:

```bash
python -m src.sorting              # sorts a sample list with every algorithm
python -m src.sorting --bench 2000 # times every algorithm on 2000 random integers
```

Sample benchmark output (2000 random integers):

```
Algorithm      Time (ms)  Correct
--------------------------------
radix               0.61  yes
quick               1.18  yes
counting            1.43  yes
merge               1.96  yes
shell               2.24  yes
heap                2.45  yes
bucket              4.57  yes
selection          43.43  yes
insertion          48.95  yes
bubble            104.27  yes
built-in            0.17  yes
```

You can see the O(n²) algorithms fall far behind as the input grows.

## 🧪 Tests

```bash
python -m pytest tests/test_sorting.py -v
```

The tests check every algorithm against Python's `sorted()` on empty lists, single items, duplicates, already sorted and reversed lists, negative numbers, random data, descending order, strings (comparison sorts) and floats (bucket sort). They also check that the input list is left unchanged.
