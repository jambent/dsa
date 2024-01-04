def python_sort(input_list):
    """
    Uses built-in Python 'sorted' method to sort list of integers

    Args:
        input_list: target list
    Returns:
        Sorted list
    Raises:
        TypeError if any element of input list is not an integer
    """
    if len(input_list) == 0:
        return []

    for element in input_list:
        if not isinstance(element, int):
            raise TypeError('Only integers are allowed in the input list')

    working_list = sorted(input_list)

    return working_list
