"""EX07 - Dictionary Functions."""

__author__ = "713138586"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Takes a dictionary and returns a dictionary with keys and values inverted."""
    inverted: dict[str, str] = {}
    for idx in a:
        if a[idx] not in inverted:
            inverted[a[idx]] = idx
        else:
            raise KeyError("Duplicate keys found")
    return inverted


def favorite_color(b: dict[str, str]) -> str:
    """Returns the color value that appears most frequently."""
    max: dict[str, int] = {}
    most_frequent: str = ""
    max_num: int = 0
    for idx in b:
        if b[idx] not in max:
            max[b[idx]] = 1
        else:
            max[b[idx]] += 1
    for idx in max:
        if max[idx] > max_num:
            max_num = max[idx]
            most_frequent = idx
    return most_frequent


def count(c: list[str]) -> dict[str, int]:
    """Counts the number of times an item occurs in a list."""
    counter: dict[str, int] = {}
    for idx in c:
        if idx in counter:
            counter[idx] += 1
        else:
            counter[idx] = 1
    return counter