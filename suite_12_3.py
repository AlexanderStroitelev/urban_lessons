import unittest

from test_12_3 import RunnerTest
from test_12_3 import TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
