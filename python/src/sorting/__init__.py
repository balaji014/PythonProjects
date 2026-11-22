"""Sorting techniques implemented from scratch in pure Python."""

from .comparison_sorts import (
    bubble_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    selection_sort,
    shell_sort,
)
from .non_comparison_sorts import bucket_sort, counting_sort, radix_sort

# Name -> function, handy for demos, benchmarks and tests.
ALGORITHMS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "shell": shell_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "counting": counting_sort,
    "radix": radix_sort,
    "bucket": bucket_sort,
}

__all__ = list(f"{name}_sort" for name in ALGORITHMS) + ["ALGORITHMS"]
