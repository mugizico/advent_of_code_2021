"""
calculate if the number of measurements is increasing
and return a count of how many times
it has increased.
"""
from collections import deque
from itertools import islice
from typing import Iterator, Iterable


def _read_measurements() -> list:
    with open("day_1_input.txt", "r") as f:
        return [int(line) for line in f]


# TODO: use more-itertools' sliding_window() util, instead
# of reinventing the wheel
def _make_sliding_window(iterable: Iterable, size: int) -> Iterator:
    it = iter(iterable)
    window = deque(islice(it, size), maxlen=size)
    if len(window) == size:
        yield tuple(window)
    for element in it:
        window.append(element)
        yield tuple(window)


def calculate_increase():
    measurements_list = _read_measurements()
    increase_count = 0

    for count in range(1, len(measurements_list)):
        if measurements_list[count] > measurements_list[count - 1]:
            increase_count += 1

    return increase_count


def calculate_three_measure_window():
    measurements_list = _read_measurements()
    increase_window_count = 0
    window_it = _make_sliding_window(measurements_list, 3)
    previous = next(window_it)

    for window in window_it:
        if sum(window) > sum(previous):
            increase_window_count += 1
        previous = window
        # print(f" previous_window is now {previous}")

    return increase_window_count


if __name__ == "__main__":
    regular_count = calculate_increase()
    window_count = calculate_three_measure_window()
    print(f"increase count per measurement: {regular_count}")
    print(f"increase count with 3-measure sliding window: {window_count}")
