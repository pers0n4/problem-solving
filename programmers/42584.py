# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices: list[int]):
    answer = [0] * len(prices)
    for i, past in enumerate(prices):
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if past > prices[j]:
                break
    return answer


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            prices = [1, 2, 3, 2, 3]
            expected = [4, 3, 1, 1, 0]
            actual = solution(prices)
            self.assertEqual(actual, expected)

    unittest.main()
