"""List utils exercise."""

__author__ = "713138586"


def all(int_list: list[int], int_check: int) -> bool:
    """Checks to see if all ints are the same."""
    list_idx: int = 0
    testing_bool: bool = True
    if len(int_list) == 0:
        testing_bool = False
    else:
        while list_idx < len(int_list):
            if int_check != int_list[list_idx]:
                testing_bool = False
            list_idx += 1

    return testing_bool
    
    
def max(input: list[int]) -> int:
    """Finds the maximum number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    num_idx: int = 0
    max_num: int = input[num_idx]
    while num_idx < len(input):
        if input[num_idx] > max_num:
            max_num = input[num_idx]
        num_idx += 1
    return max_num


def is_equal(first: list[int], second: list[int]) -> bool:
    """Checks to make sure all items at a list index match that same index in the other list."""
    check_idx: int = 0
    checking_bool: bool = True
    if len(first) != len(second):
        checking_bool = False
    else:
        while check_idx < len(first) or check_idx < len(second):
            if first[check_idx] == second[check_idx]:
                check_idx += 1
            else:
                checking_bool = False
                return False
    return checking_bool