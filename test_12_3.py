import unittest

from runner_and_tournament import (
    Runner ,
    Tournament ,
)


def control_execution(method):
    """Декоратор для выполнения или пропуска теста в зависимости от значения is_frozen."""

    def wrapper(self, *args, **kwargs):
        if not self.is_frozen:
            return method(self, *args, **kwargs)
        else:
            self.skipTest("Тесты в этом кейсе заморожены")

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False  # Контроль выполнения тестов

    @control_execution
    def test_walk(self):
        runner = Runner("Test Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @control_execution
    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @control_execution
    def test_challenge(self):
        runner1 = Runner("Runner")
        runner2 = Runner("Walker")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Контроль выполнения тестов

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_name, result in cls.all_results.items():
            formatted_result = cls.format_results(result)
            print(formatted_result)

    @staticmethod
    def format_results(results):
        formatted = (
            "{"
            + ", ".join([f"{place}: {runner}" for place, runner in results.items()])
            + "}"
        )
        return formatted

    @control_execution
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_usain_and_nick"] = results

        last_runner_name = results[max(results.keys())].name
        self.assertTrue(
            last_runner_name == "Ник", f"Ожидался Ник, а был {last_runner_name}"
        )

    @control_execution
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_andrey_and_nick"] = results

        last_runner_name = results[max(results.keys())].name
        self.assertTrue(
            last_runner_name == "Ник", f"Ожидался Ник, а был {last_runner_name}"
        )

    @control_execution
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        TournamentTest.all_results["test_usain_andrey_and_nick"] = results

        last_runner_name = results[max(results.keys())].name
        self.assertTrue(
            last_runner_name == "Ник", f"Ожидался Ник, а был {last_runner_name}"
        )


if __name__ == "__main__":
    unittest.main()
