def sum_recursive(numbers):
    if not numbers:
        return 0

    return numbers[0] + sum_recursive(numbers[1:])


print(sum_recursive([1, 2, 3]))
