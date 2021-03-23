def count(item_list):
    if not item_list:
        return 0

    return 1 + count(item_list[1:])


print(count([0] * 3))
