from random import randint

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from python_sort import python_sort
from run_stats_profiler import run_stats_profiler


if __name__ == '__main__':
    test_data = [randint(-100,100) for _ in range(0,10000)]
    sort_functions = [bubble_sort,selection_sort,insertion_sort,python_sort]

    for function in sort_functions:
        run_stats_profiler(function,test_data)
