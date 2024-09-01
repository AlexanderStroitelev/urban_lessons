import unittest

from module12.runner import Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner("Test Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner")
        runner2 = Runner("Walker")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
