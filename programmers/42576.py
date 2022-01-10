# 완주하지 못한 선수
def solution(participant: list[str], completion: list[str]):
    players: dict[str, int] = {}

    for p in participant:
        players[p] = players.get(p, 0) + 1

    for c in completion:
        players[c] -= 1

    return list(filter(lambda p: p[1] != 0, players.items())).pop()[0]


if __name__ == "__main__":
    for result in map(
        solution,
        [
            ["leo", "kiki", "eden"],
            ["marina", "josipa", "nikola", "vinko", "filipa"],
            ["mislav", "stanko", "mislav", "ana"],
        ],
        [
            ["eden", "kiki"],
            ["josipa", "filipa", "marina", "nikola"],
            ["stanko", "ana", "mislav"],
        ],
    ):
        print(result)
