# 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/42839
def solution(numbers: str):
    from itertools import permutations

    flat_map = lambda f, xs: (y for x in xs for y in f(x))
    unique_numbers = list(
        filter(
            lambda number: number >= 2,
            set(
                flat_map(
                    lambda i: tuple(
                        map(lambda p: int("".join(p)), permutations(numbers, i + 1))
                    ),
                    range(len(numbers)),
                )
            ),
        )
    )

    prime_map = dict({number: True for number in unique_numbers})
    for n in unique_numbers:
        m = int(n ** 0.5)
        for j in range(2, m + 1):
            if n % j == 0:
                prime_map[n] = False
                break

    return list(prime_map.values()).count(True)


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            numbers = "17"
            expected = 3
            actual = solution(numbers)
            self.assertEqual(actual, expected)

        def test_case2(self):
            numbers = "011"
            expected = 2
            actual = solution(numbers)
            self.assertEqual(actual, expected)

    unittest.main()
