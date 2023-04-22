import collections


def print_count_simple_repetitions(message: str) -> None:
    counter = collections.Counter(message)
    res = sum(counter.values()) - len([i for i in counter.values() if i == 1])
    print(res)


def get_dict_repetitions(data: list) -> dict:
    counter = collections.Counter(data)
    return dict(counter)


def fun_1() -> None:
    set_1, set_2 = {1, 2, 3, 4, 5}, {1, 3, 5, 7, 9}
    found = len(set_1 & set_2)
    print(found)


