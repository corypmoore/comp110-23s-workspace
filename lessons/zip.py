"""Practice with dicts."""


def zip(words: list[str], nums: list[int]) -> dict[str, int]:
    """Creates a dictionary from two lists"""
    words_len: int = len(words)
    nums_len: int = len(nums)
    zip_dict: dict[str, int] = {}
    if words_len != nums_len or words_len == 0 or nums_len == 0:
        return zip_dict
    else:
        for idx in range(0, words_len):
            zip_dict[words[idx]] = nums[idx]
    return zip_dict