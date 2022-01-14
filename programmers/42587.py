# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities: list[int], location: int):
    waiting_list = []
    priority_sequence = list(enumerate(priorities))
    while priority_sequence:
        index, candidate = priority_sequence.pop(0)
        for _, priority in priority_sequence:
            if priority > candidate:
                priority_sequence.append((index, candidate))
                break
        else:
            waiting_list.append((index, candidate))
    return list(map(lambda x: x[0], waiting_list)).index(location) + 1


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            priorities = [2, 1, 3, 2]
            location = 2
            expected = 1
            actual = solution(priorities, location)
            self.assertEqual(actual, expected)

        def test_case2(self):
            priorities = [1, 1, 9, 1, 1, 1]
            location = 0
            expected = 5
            actual = solution(priorities, location)
            self.assertEqual(actual, expected)

    unittest.main()
