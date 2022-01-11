# 위장
def solution(clothes: list[list[str]]):
    from functools import reduce

    hash_table: dict[str, int] = {}
    for _, category in clothes:
        hash_table.setdefault(category, 1)
        hash_table[category] += 1

    return reduce(lambda x, y: x * y, hash_table.values()) - 1


if __name__ == "__main__":
    for result in map(
        solution,
        [
            [
                ["yellowhat", "headgear"],
                ["bluesunglasses", "eyewear"],
                ["green_turban", "headgear"],
            ],
            [
                ["crowmask", "face"],
                ["bluesunglasses", "face"],
                ["smoky_makeup", "face"],
            ],
        ],
    ):
        print(result)
