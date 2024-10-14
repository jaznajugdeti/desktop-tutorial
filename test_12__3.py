# Часть 1. TestSuit.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
# is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
# 'Тесты в этом кейсе заморожены'.
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)


    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
import unittest

class TournamentTest(unittest.TestCase):

    # tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        cls.all_results = {}

    # setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который
    # будут сохраняться результаты всех тестов.
    @unittest.skipIf(True, 'работает')
    def setUp(self):
        h_run = Runner('Усэйн', 10)
        a_run = Runner('Андрей', 9)
        n_run = Runner('Ник', 3)

# tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    @unittest.skipIf(True, 'работает')
    def test_run(self):
        test_r1 = Tournament(90, self.h_run, self.n_run)
        result = test_r1.start()
        self.assertTrue(result[list(result.keys())[-1]])
        self.all_results['test_r1'] = result
class RunnerTest(unittest.TestCase):

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
    @unittest.skipIf(False, 'пропуск')
    def test_walk(self):
        run_ = Runner('run1')
        for i in range(10):
            run_.walk()
        self.assertEqual(run_.distance, 50)

# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
    @unittest.skipIf(False, 'пропуск')
    def test_run(self):
        run_2 = Runner('run2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз
# у объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте
# метод assertNotEqual, чтобы убедится в неравенстве результатов.
    @unittest.skipIf(False, 'пропуск')
    def test_challenge(self):
        run_3 = Runner('run3')
        run_4 = Runner('run4')
        for _ in range(10):
            run_3.walk()
            run_4.run()
        self.assertNotEqual(run_3.distance, run_4.distance)
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.


# Создайте модуль suite_12_3.py для описания объекта TestSuite. Укажите на него переменной
# с произвольным названием.
# Добавьте тесты RunnerTest и TournamentTest в этот TestSuit.
# Создайте объект класса TextTestRunner, с аргументом verbosity=2.
# Часть 2. Пропуск тестов.
# Классы RunnerTest дополнить атрибутом is_frozen = False и TournamentTest атрибутом is_frozen = True.
# Напишите соответствующий декоратор к каждому методу (кроме @classmethod), который при значении
# is_frozen = False будет выполнять тесты, а is_frozen = True - пропускать и выводить сообщение
# 'Тесты в этом кейсе заморожены'.
# Таким образом вы сможете контролировать пропуск всех тестов в TestCase изменением всего одного атрибута.
# Запустите TestSuite и проверьте полученные результаты тестов из обоих TestCase.
# Пример результата выполнения тестов:
# Вывод на консоль:
# test_challenge (tests_12_3.RunnerTest.test_challenge) ... ok
# test_run (tests_12_3.RunnerTest.test_run) ... ok
# test_walk (tests_12_3.RunnerTest.test_walk) ... ok
# test_first_tournament (tests_12_3.TournamentTest.test_first_tournament) ... skipped
# 'Тесты в этом кейсе заморожены'
# test_second_tournament (tests_12_3.TournamentTest.test_second_tournament) ... skipped
# 'Тесты в этом кейсе заморожены'
# test_third_tournament (tests_12_3.TournamentTest.test_third_tournament) ... skipped
# 'Тесты в этом кейсе заморожены'
# ----------------------------------------------------------------------
# Ran 6 tests in 0.000s OK (skipped=3)
