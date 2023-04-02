"""List utils exercise."""

__author__ = "713138586"


def only_evens(input_list: list[int]) -> list[int]:
    """Creates a new list of only even numbers."""
    evens: list[int] = list()
    list_idx: int = 0
    while list_idx < len(input_list):
        if input_list[list_idx] % 2 == 0:
            evens.append(input_list[list_idx])
        list_idx += 1
    return evens


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Combines two lists consecutively.""" 
    big_list: list[int] = list()
    i: int = 0
    i_s: int = 0
    while i < len(first_list):
        big_list.append(first_list[i])
        i += 1
    while i_s < len(second_list):
        big_list.append(second_list[i_s])
        i_s += 1
    return big_list


def sub(a_list: list[int], x: int, y: int):
    """Creates a new list using only list items in specified range."""
    sub_list: list[int] = list()
    empty_list: list[int] = list()
    start_len: int = len(a_list)
    if start_len == 0 or x > start_len or y <= 0:
        return empty_list
    else:
        if x < 0:
            x = 0
            if y >= start_len:
                y = start_len
                for idx in range(x, y):
                    sub_list.append(a_list[idx])
            else:
                for idx in range(x, y):
                    sub_list.append(a_list[idx])
        else:
            if y >= start_len:
                y = start_len
                for idx in range(x, y):
                    sub_list.append(a_list[idx])
            else:
                for idx in range(x, y):
                    sub_list.append(a_list[idx])
        return sub_list