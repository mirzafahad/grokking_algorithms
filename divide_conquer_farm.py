def biggest_square_plot(length, width):
    if length < width:
        length, width = width, length

    if length % width == 0:
        return width

    return biggest_square_plot(width, length % width)


print(biggest_square_plot(240, 240))
