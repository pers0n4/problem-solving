# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers: list[int]):
    return "".join(sorted(map(str, numbers), key=lambda x: x * 3, reverse=True))


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            numbers = [6, 10, 2]
            expected = "6210"
            actual = solution(numbers)
            self.assertEqual(actual, expected)

        def test_case2(self):
            numbers = [3, 30, 34, 5, 9]
            expected = "9534330"
            actual = solution(numbers)
            self.assertEqual(actual, expected)

    unittest.main()
