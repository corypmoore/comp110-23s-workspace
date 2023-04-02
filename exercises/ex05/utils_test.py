"""List utils exercise test."""

__author__ = "713138586"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty_evens() -> None:
    """Testing output of an empty list."""
    assert only_evens([]) == []


def test_one_element_evens() -> None:
    """Testing output of a list only containing one int."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]
    
    
def test_many_evens() -> None:
    """Testing output in a list that meets normal use cases."""
    test_list: list[int] = [2, 3, 4, 7, 8]
    assert only_evens(test_list) == [2, 4, 8]


def test_empty_con() -> None:
    """Testing output of an empty list."""
    assert concat([], []) == []


def test_one_element_con() -> None:
    """Testing output of two lists only containing one int each."""
    test_list_a: list[int] = [2]
    test_list_b: list[int] = [3]
    assert concat(test_list_a, test_list_b) == [2, 3]


def test_many_con() -> None:
    """Testing output in lists that meet normal use cases."""
    test_list_a: list[int] = [2, 3, 4, 7, 8]
    test_list_b: list[int] = [3, 4, 6, 9]
    assert concat(test_list_a, test_list_b) == [2, 3, 4, 7, 8, 3, 4, 6, 9]


def test_empty_sub() -> None:
    """Testing output of an empty list."""
    assert sub([], 2, 3) == []

  
def test_many_with_negatives_sub() -> None:
    """Testing output if start index is negative."""
    test_list: list[int] = [2, 4, 7, 9, 10]
    assert sub(test_list, -4, 3) == [2, 4, 7]

    
def test_many_with_high_index_sub() -> None:
    """Testing output if end index is greater than the length of the input list."""
    test_list: list[int] = [2, 4, 7, 9, 10]
    assert sub(test_list, 1, 9) == [4, 7, 9, 10]