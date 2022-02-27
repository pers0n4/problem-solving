# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown: int, yellow: int):
    size = brown + yellow
    candidates = [
        [size // i, i] for i in range(3, int(size ** 0.5) + 1) if size % i == 0
    ]

    return next(
        filter(
            lambda candidate: (candidate[0] - 2) * (candidate[1] - 2) == yellow,
            candidates,
        )
    )


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            brown = 10
            yellow = 2
            expected = [4, 3]
            actual = solution(brown, yellow)
            self.assertEqual(actual, expected)

        def test_case2(self):
            brown = 8
            yellow = 1
            expected = [3, 3]
            actual = solution(brown, yellow)
            self.assertEqual(actual, expected)

        def test_case3(self):
            brown = 24
            yellow = 24
            expected = [8, 6]
            actual = solution(brown, yellow)
            self.assertEqual(actual, expected)

    unittest.main()
