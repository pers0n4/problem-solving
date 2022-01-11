# 전화번호 목록
def solution(phone_book: list[str]):
    hash_table = dict(map(lambda x: (x, True), phone_book))
    for phone in phone_book:
        key = ""
        for number in phone[:-1]:
            key += number
            if hash_table.get(key, False):
                return False
    return True


if __name__ == "__main__":
    for result in map(
        solution,
        [
            ["119", "97674223", "1195524421"],
            ["123", "456", "789"],
            ["12", "123", "1235", "567", "88"],
        ],
    ):
        print(result)
