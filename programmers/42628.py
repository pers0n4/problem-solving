# 이중우선순위큐
# https://programmers.co.kr/learn/courses/30/lessons/42628
def solution(operations: list[str]):
    import heapq as hq

    heap: list[int] = []
    for operation in operations:
        action, value = operation.split()
        if action == "I":
            hq.heappush(heap, int(value))
        elif heap:
            target = max(heap) if int(value) > 0 else min(heap)
            heap.remove(target)
    return [max(heap), min(heap)] if heap else [0, 0]


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            operations = ["I 16", "D 1"]
            expected = [0, 0]
            actual = solution(operations)
            self.assertEqual(actual, expected)

        def test_case2(self):
            operations = ["I 7", "I 5", "I -5", "D -1"]
            expected = [7, 5]
            actual = solution(operations)
            self.assertEqual(actual, expected)

    unittest.main()
