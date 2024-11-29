import runner_and_tournament
from unittest import TestCase


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = dict()

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner_2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner_3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            print(cls.all_results[i])

    def testTournament_1(self):
        t_distance = runner_and_tournament.Tournament(90, self.runner_3, self.runner_1)
        all_results = t_distance.start()
        q = {}
        k = 1
        for i in all_results:
            q[k] = str(all_results[i])
            k += 1
        self.all_results[1] = q
        self.assertIs(q[len(q)], 'Ник')

    def testTournament_2(self):
        t_distance = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        all_results = t_distance.start()
        q = {}
        k = 1
        for i in all_results:
            q[k] = str(all_results[i])
            k += 1
        self.all_results[2] = q
        self.assertIs(q[len(q)], 'Ник')

    def testTournament_3(self):
        t_distance = runner_and_tournament.Tournament(90, self.runner_1, self.runner_3, self.runner_2)
        all_results = t_distance.start()
        q = {}
        k = 1
        for i in all_results:
            q[k] = str(all_results[i])
            k += 1
        self.all_results[3] = q
        self.assertIs(q[len(q)], 'Ник')
