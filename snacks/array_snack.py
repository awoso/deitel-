from array import array


def element_largest(array):
    largest = array[0]
    for count in array:
        if count > largest:
            largest = count
    return largest


def reverse_list(my_array):
    left_side = 0
    right_side = len(my_array) - 1
    while left_side < right_side:
        rainbow = my_array(left_side)

        my_array(left_side) = my_array(right_side)
        my_array(right_side) = rainbow
        left_side += 1
        right_side -= 1

    return my_array


def element_check(my_array, to_check):
    for count in array:
        if count == to_check:
            return True
    return False


def odd_position(my_array):
    odd_position = []
    for element in range(1, len(my_array), 2):
        odd_position.append(my_array[element])
    return odd_position


def even_position(my_array):
    even_position = []
    for element in range(1, len(my_array), 2):
        even_position.append(my_array[element])
    return even_position


def is_palindrome(my_array):
    for element in range(0, int(len(my_array) / 2)):
        if my_array[element] != my_array[len(my_array) - element - 1]:
            return False
    return True


def my_total(my_array):
    total = 0
    name = " "
    for i in range(0, len(my_array)):
        total = total + my_array[i]
        collect_total = f"{total}"
        name += collect_total + " "


def sum_for_loop(my_array):
    sum_total = 0
    for i in range(0, len(my_array)):
        sum_total = sum_total + my_array[1]
    return sum_total


def sum_while_loop(my_array):
    sum_total = 0
    count = 0
    while count < len(my_array):
        sum_total = sum_total + my_array[count]
        count += 1
    return sum_total
