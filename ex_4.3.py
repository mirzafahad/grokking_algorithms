def max_recursive(item_list):
    if len(item_list) == 2:
        if item_list[0] > item_list[1]:
            return item_list[0]
        return item_list[1]

    sub_max = max_recursive(item_list[1:])

    if sub_max < item_list[0]:
        return item_list[0]

    return sub_max


print(max_recursive([3, 5, 9, 1, 4, 1]))
