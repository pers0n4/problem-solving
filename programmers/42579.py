# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres: list[str], plays: list[int]):
    genre_table: dict[str, list[tuple[int, int]]] = {}
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_table.setdefault(genre, [])
        genre_table[genre].append((index, play))

    best_genres = sorted(
        genre_table,
        key=lambda genre: sum(map(lambda song: song[1], genre_table[genre])),
        reverse=True,
    )
    best_albums = map(
        lambda genre: map(
            lambda song: song[0],
            sorted(genre_table[genre], key=lambda song: song[1], reverse=True)[:2],
        ),
        best_genres,
    )

    return [song for genre in best_albums for song in genre]


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            genres = ["classic", "pop", "classic", "classic", "pop"]
            plays = [500, 600, 150, 800, 2500]
            self.assertEqual(solution(genres, plays), [4, 1, 3, 0])

    unittest.main()
