# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length: int, weight: int, truck_weights: list[int]):
    answer = 0
    index = 0
    bridge = [0] * bridge_length
    while truck_weights:
        bridge[index] = 0
        if sum(bridge) + truck_weights[0] <= weight:
            bridge[index] = truck_weights.pop(0)
        answer += 1
        index = answer % bridge_length
    return answer + bridge_length


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            bridge_length = 2
            weight = 10
            truck_weights = [7, 4, 5, 6]
            expected = 8
            actual = solution(bridge_length, weight, truck_weights)
            self.assertEqual(actual, expected)

        def test_case2(self):
            bridge_length = 100
            weight = 100
            truck_weights = [10]
            expected = 101
            actual = solution(bridge_length, weight, truck_weights)
            self.assertEqual(actual, expected)

        def test_case3(self):
            bridge_length = 100
            weight = 100
            truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
            expected = 110
            actual = solution(bridge_length, weight, truck_weights)
            self.assertEqual(actual, expected)

    unittest.main()
