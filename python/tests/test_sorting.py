import random

import pytest

from src.sorting import ALGORITHMS, bucket_sort, counting_sort, radix_sort

CASES = [
    [],
    [1],
    [2, 1],
    [5, 2, 9, 1, 5, 6],
    [3, 3, 3, 3],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [0, -1, -50, 7, 100, -3, 0],
    [1000, 1, 100, 10, 10000],
]


@pytest.mark.parametrize("name", ALGORITHMS)
@pytest.mark.parametrize("data", CASES)
def test_sorts_ascending(name, data):
    assert ALGORITHMS[name](data) == sorted(data)


@pytest.mark.parametrize("name", ALGORITHMS)
@pytest.mark.parametrize("data", CASES)
def test_sorts_descending(name, data):
    assert ALGORITHMS[name](data, reverse=True) == sorted(data, reverse=True)


@pytest.mark.parametrize("name", ALGORITHMS)
def test_random_input(name):
    rng = random.Random(42)
    data = [rng.randint(-1000, 1000) for _ in range(300)]
    assert ALGORITHMS[name](data) == sorted(data)


@pytest.mark.parametrize("name", ALGORITHMS)
def test_input_is_not_modified(name):
    data = [3, 1, 2]
    ALGORITHMS[name](data)
    assert data == [3, 1, 2]


@pytest.mark.parametrize("name", ALGORITHMS)
def test_accepts_any_iterable(name):
    assert ALGORITHMS[name]((x for x in (3, 1, 2))) == [1, 2, 3]


@pytest.mark.parametrize(
    "name", ["bubble", "selection", "insertion", "shell", "merge", "quick", "heap"]
)
def test_comparison_sorts_handle_strings(name):
    words = ["pear", "apple", "fig", "banana"]
    assert ALGORITHMS[name](words) == sorted(words)


def test_bucket_sort_handles_floats():
    data = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51, -1.5, 3.75]
    assert bucket_sort(data) == sorted(data)


@pytest.mark.parametrize("func", [counting_sort, radix_sort])
def test_integer_only_sorts_reject_floats(func):
    with pytest.raises(TypeError):
        func([1.5, 2.0])
