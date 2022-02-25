# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers: list[int]):
    from itertools import cycle

    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    ]

    correct_answers = list(
        map(
            lambda pair: len(list(filter(lambda x: x[0] == x[1], pair))),
            [zip(answers, cycle(pattern)) for pattern in patterns],
        )
    )

    return [
        i + 1
        for i, answer in enumerate(correct_answers)
        if answer == max(correct_answers)
    ]


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            answers = [1, 2, 3, 4, 5]
            expected = [1]
            actual = solution(answers)
            self.assertEqual(actual, expected)

        def test_case2(self):
            answers = [1, 3, 2, 4, 2]
            expected = [1, 2, 3]
            actual = solution(answers)
            self.assertEqual(actual, expected)

    unittest.main()
