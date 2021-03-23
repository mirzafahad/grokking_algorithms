def find_smallest(list_of_items):
    smallest_index = 0
    smallest_item = list_of_items[0]

    for index in range(1, len(list_of_items)):
        if list_of_items[index] < smallest_item:
            smallest_index = index
            smallest_item = list_of_items[index]

    return smallest_index


def selection_sort(items):
    sorted_list = []
    # Note: if you don't want to alter the
    # passing list, deepcopy the list
    while items:
        index = find_smallest(items)
        sorted_list.append(items.pop(index))

    return sorted_list


print(selection_sort([5, 3, 6, 2, 10]))
