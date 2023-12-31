import copy

def bubble_sort(input_list):
    """
    Implements bubble sort algorithm for array of integers

    Args:
        input_array: target list containing integers
    Returns:
        Sorted list of integers
    Raises:
        TypeError if any element of input list is not an integer
    """
    for element in input_list:
        if type(element) is not int:
            raise TypeError('Only integers are allowed in the input list')

    working_list = copy.deepcopy(input_list)
    working_list_length = len(working_list)
    
    numbers_swapped_on_pass = True
    try:
        while numbers_swapped_on_pass:
            numbers_swapped_on_pass = False
            for i in range (working_list_length-1):
                if working_list[i] > working_list[i+1]:
                    working_list[i],working_list[i+1] = \
                        working_list[i+1],working_list[i]
                    numbers_swapped_on_pass = True
    except Exception as e:
        print(f'Unexpected error encountered during sorting: {e}')
    
    return working_list



