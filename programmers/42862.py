# 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n: int, lost: list[int], reserve: list[int]):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)

    return n - len(lost_set)


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            n = 5
            lost = [2, 4]
            reserve = [1, 3, 5]
            expected = 5
            actual = solution(n, lost, reserve)
            self.assertEqual(actual, expected)

        def test_case2(self):
            n = 5
            lost = [2, 4]
            reserve = [3]
            expected = 4
            actual = solution(n, lost, reserve)
            self.assertEqual(actual, expected)

        def test_case3(self):
            n = 3
            lost = [3]
            reserve = [1]
            expected = 2
            actual = solution(n, lost, reserve)
            self.assertEqual(actual, expected)

    unittest.main()
