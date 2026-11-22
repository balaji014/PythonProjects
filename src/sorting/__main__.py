"""Demo and benchmark for the sorting algorithms.

Run from the repository root:

    python -m src.sorting              # demo on a small list
    python -m src.sorting --bench 2000 # time every algorithm on 2000 numbers
"""

import argparse
import random
import time

from . import ALGORITHMS


def demo() -> None:
    sample = [64, 34, 25, 12, 22, 11, 90, -5, 0, 22]
    print(f"Input: {sample}\n")
    for name, func in ALGORITHMS.items():
        print(f"{name + ' sort':<16} -> {func(sample)}")
    print(f"\n{'quick (desc)':<16} -> {ALGORITHMS['quick'](sample, reverse=True)}")


def bench(size: int) -> None:
    data = [random.randint(-10_000, 10_000) for _ in range(size)]
    expected = sorted(data)
    print(f"Sorting {size} random integers\n")
    print(f"{'Algorithm':<12}{'Time (ms)':>12}  Correct")
    print("-" * 32)
    results = []
    for name, func in ALGORITHMS.items():
        start = time.perf_counter()
        out = func(data)
        ms = (time.perf_counter() - start) * 1000
        results.append((ms, name, out == expected))
    for ms, name, ok in sorted(results):
        print(f"{name:<12}{ms:>12.2f}  {'yes' if ok else 'NO'}")

    start = time.perf_counter()
    sorted(data)
    print(f"{'built-in':<12}{(time.perf_counter() - start) * 1000:>12.2f}  yes")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sorting techniques demo")
    parser.add_argument("--bench", type=int, metavar="N",
                        help="benchmark all algorithms on N random integers")
    args = parser.parse_args()
    if args.bench:
        bench(args.bench)
    else:
        demo()


if __name__ == "__main__":
    main()
