"""EX07 - Dictionary Functions Tests."""

__author__ = "713138586"

from exercises.ex07.dictionary import invert, count, favorite_color


def test_empty_invert() -> None:
    """Testing output of an empty dictionary."""
    assert invert({}) == {}


def test_single_invert() -> None:
    """Testing output of a dictionary only containing one item."""
    test_dict: dict[str, str] = {"apple": "cat"}
    assert invert(test_dict) == {"cat": "apple"}
    
    
def test_normal_invert() -> None:
    """Testing output in a dictionary that meets normal use cases."""
    test_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_empty_count() -> None:
    """Testing output of an empty list."""
    assert count([]) == {}


def test_single_count() -> None:
    """Testing output of a list only containing one str."""
    test_list: list[str] = ["dog"]
    assert count(test_list) == {"dog": 1}


def test_normal_count() -> None:
    """Testing output in a list that meet normal use cases."""
    test_list: list[str] = ["dog", "cat", "horse", "dog"]
    assert count(test_list) == {"dog": 2, "cat": 1, "horse": 1}


def test_empty_favorite_color() -> None:
    """Testing output of an empty dict."""
    assert favorite_color({}) == ""

  
def test_tie_favorite_color() -> None:
    """Testing output if two colors have the same frequency to ensure first color listed is returned."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Cory": "yellow"}
    assert favorite_color(test_dict) == "yellow"

    
def test_normal_favorite_color() -> None:
    """Testing output of a normal use case."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Cory": "orange"}
    assert favorite_color(test_dict) == "blue"