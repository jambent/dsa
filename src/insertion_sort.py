import copy


def insertion_sort(input_list):
    """
    Implements insertion sort algorithm for array of integers

    Args:
        input_list: target list containing integers
    Returns:
        Sorted list of integers
    Raises:
        TypeError if any element of input list is not an integer
    """
    input_list_length = len(input_list)
    if input_list_length == 0:
        return []

    for element in input_list:
        if not isinstance(element, int):
            raise TypeError('Only integers are allowed in the input list')

    working_list = copy.deepcopy(input_list)

    if input_list_length == 1:
        return working_list

    try:
        for i in range(1, input_list_length):
            fixed_comparison_value = working_list[i]
            to_be_compared_to_index = i - 1

            while to_be_compared_to_index >= 0:
                if (working_list[to_be_compared_to_index]
                        > fixed_comparison_value):
                    working_list[to_be_compared_to_index + 1] = \
                        working_list[to_be_compared_to_index]
                    to_be_compared_to_index -= 1
                else:
                    break
            working_list[to_be_compared_to_index + 1] = fixed_comparison_value
    except Exception as e:
        print(f'Unexpected error encountered during sorting: {e}')

    return working_list
