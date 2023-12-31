import copy


def selection_sort(input_list):
    if input_list == []:
        return []

    for element in input_list:
        if not isinstance(element, int):
            raise TypeError('Only integers are allowed in the input list')

    working_list = copy.deepcopy(input_list)
    working_list_length = len(working_list)

    lowest_value_index = 0
    numbers_swapped = False

    for i in range(working_list_length - 1):
        lowest_value_index = i
        numbers_swapped = False
        for j in range(i, working_list_length):
            if working_list[j] < working_list[lowest_value_index]:
                lowest_value_index = j
                numbers_swapped = True
        if numbers_swapped:
            working_list[i], working_list[lowest_value_index] \
                = working_list[lowest_value_index], working_list[i]

    return working_list
