# 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses: list[int], speeds: list[int]):
    from math import ceil

    remains_progresses = map(lambda progress: 100 - progress, progresses)
    remains_day = [
        ceil(remains_progress / speed)
        for remains_progress, speed in zip(remains_progresses, speeds)
    ]

    batch = []
    while remains_day:
        remain = remains_day.pop(0)
        count = 1
        while remains_day and remain >= remains_day[0]:
            remains_day.pop(0)
            count += 1
        batch.append(count)

    return batch


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            progresses = [93, 30, 55]
            speeds = [1, 30, 5]
            expected = [2, 1]
            actual = solution(progresses, speeds)
            self.assertEqual(actual, expected)

        def test_case2(self):
            progresses = [95, 90, 99, 99, 80, 99]
            speeds = [1, 1, 1, 1, 1, 1]
            expected = [1, 3, 2]
            actual = solution(progresses, speeds)
            self.assertEqual(actual, expected)

    unittest.main()
