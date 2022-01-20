# K번째수
# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array: list[int], commands: list[list[int]]):
    return list(
        map(
            lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1],
            commands,
        )
    )


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            array = [1, 5, 2, 6, 3, 7, 4]
            commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
            expected = [5, 6, 3]
            actual = solution(array, commands)
            self.assertEqual(actual, expected)

    unittest.main()
