def binary_search(list_of_items, item):
    if not isinstance(list_of_items, list):
        raise TypeError
    if not list_of_items:
        return None

    low = 0
    high = len(list_of_items) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_item = list_of_items[mid]

        if mid_item == item:
            return mid
        elif mid_item > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


a_list = [1, 3, 5, 7, 9]
print(binary_search(a_list, 5))
print(binary_search(a_list, -1))
