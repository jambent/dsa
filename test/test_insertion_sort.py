import pytest
import copy

from src.insertion_sort import insertion_sort


def test_that_list_returned():
    result = insertion_sort([])

    assert isinstance(result, list)


def test_that_empty_list_returned_if_input_empty():
    result = insertion_sort([])

    assert result == []


def test_that_list_contains_only_integers():
    result = insertion_sort([2, 8, 4, 9, 1])

    for number in result:
        assert isinstance(number, int)


def test_that_list_of_2_elements_sorted_correctly():
    result = insertion_sort([2, 8])

    assert result == [2, 8]

    result = insertion_sort([4, 3])

    assert result == [3, 4]


def test_that_list_of_3_elements_sorted_correctly():
    result = insertion_sort([1, 2, 4])

    assert result == [1, 2, 4]

    result = insertion_sort([6, 4, 3])

    assert result == [3, 4, 6]


def test_that_larger_list_sorted_correctly():
    result = insertion_sort([2, 8, 4, 9, 1])

    assert result == [1, 2, 4, 8, 9]


def test_that_input_list_not_mutated():
    input = [12, 5, 67, 34, -4]
    input_copy = copy.deepcopy(input)
    result = insertion_sort(input)

    assert result == [-4, 5, 12, 34, 67]
    assert input_copy == input
    assert input_copy is not input


def test_type_error_raised_if_input_contains_non_integers():
    with pytest.raises(TypeError, match='Only integers are allowed'):
        insertion_sort([2, 8, 'b', 9, 1])
