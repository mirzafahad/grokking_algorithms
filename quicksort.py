def quicksort(num_list):
    list_len = len(num_list)
    if list_len < 2:
        return num_list

    mid_index = list_len // 2
    pivot = num_list[mid_index]

    less_nums = []
    greater_nums = []
    for i, num in enumerate(num_list):
        if i == mid_index:
            continue
        if num > pivot:
            greater_nums.append(num)
        else:
            less_nums.append(num)

    return quicksort(less_nums) + [pivot] + quicksort(greater_nums)


print(quicksort([10, 5, 2, 3]))
