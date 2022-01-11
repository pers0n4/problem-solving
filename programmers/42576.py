# 완주하지 못한 선수
def solution(participant: list[str], completion: list[str]):
    players: dict[str, int] = {}

    for p in participant:
        players[p] = players.get(p, 0) + 1

    for c in completion:
        players[c] -= 1

    return list(filter(lambda p: p[1] != 0, players.items())).pop()[0]


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            participant = ["leo", "kiki", "eden"]
            completion = ["eden", "kiki"]
            self.assertEqual(solution(participant, completion), "leo")

        def test_case2(self):
            participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
            completion = ["josipa", "filipa", "marina", "nikola"]
            self.assertEqual(solution(participant, completion), "vinko")

        def test_case3(self):
            participant = ["mislav", "stanko", "mislav", "ana"]
            completion = ["stanko", "ana", "mislav"]
            self.assertEqual(solution(participant, completion), "mislav")

    unittest.main()
