# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577
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
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            phone_book = ["119", "97674223", "1195524421"]
            self.assertEqual(solution(phone_book), False)

        def test_case2(self):
            phone_book = ["123", "456", "789"]
            self.assertEqual(solution(phone_book), True)

        def test_case3(self):
            phone_book = ["12", "123", "1235", "567", "88"]
            self.assertEqual(solution(phone_book), False)

    unittest.main()
