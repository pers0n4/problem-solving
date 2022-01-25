# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations: list[int]):
    for h in range(len(citations), 0, -1):
        more = list(filter(lambda c: c >= h, citations))
        less = list(filter(lambda c: c <= h, citations))
        if len(more) >= h >= len(less):
            return h
    return 0


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            citations = [3, 0, 6, 1, 5]
            expected = 3
            actual = solution(citations)
            self.assertEqual(actual, expected)

    unittest.main()
