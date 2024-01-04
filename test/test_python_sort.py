import pytest
import copy

from src.python_sort import python_sort


def test_that_list_returned():
    result = python_sort([])

    assert isinstance(result, list)


def test_that_empty_list_returned_if_input_empty():
    result = python_sort([])

    assert result == []


def test_that_list_contains_only_integers():
    result = python_sort([2, 8, 4, 9, 1])

    for number in result:
        assert isinstance(number, int)


def test_that_returned_list_sorted_correctly():
    result = python_sort([2, 8, 4, 9, 1])

    assert result == [1, 2, 4, 8, 9]


def test_that_input_list_not_mutated():
    input = [12, 5, 67, 34, -4]
    input_copy = copy.deepcopy(input)
    result = python_sort(input)

    assert result == [-4, 5, 12, 34, 67]
    assert input_copy == input
    assert input_copy is not input


def test_type_error_raised_if_input_contains_non_integers():
    with pytest.raises(TypeError, match='Only integers are allowed'):
        python_sort([2, 8, 'b', 9, 1])
