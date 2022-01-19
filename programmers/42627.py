# 디스크 컨트롤러
# https://programmers.co.kr/learn/courses/30/lessons/42627
def solution(jobs: list[list[int]]):
    task_time = schedule_time = 0
    task_length = len(jobs)
    while jobs:
        next_jobs = list(filter(lambda job: job[0] <= task_time, jobs))
        if not next_jobs:
            task_time += 1
            continue
        task = min(next_jobs, key=lambda job: job[1])
        task_time += task[1]
        schedule_time += task_time - task[0]
        jobs.remove(task)
    return schedule_time // task_length


if __name__ == "__main__":
    import unittest

    class TestSolution(unittest.TestCase):
        def test_case1(self):
            jobs = [[0, 3], [1, 9], [2, 6]]
            expected = 9
            actual = solution(jobs)
            self.assertEqual(actual, expected)

    unittest.main()
