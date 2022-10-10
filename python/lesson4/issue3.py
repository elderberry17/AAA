import unittest

from one_hot_encoder import fit_transform


class TestOHE(unittest.TestCase):
    def test_empty(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_no(self):
        exp_city = []
        emp = []
        self.assertEqual(fit_transform(emp), exp_city)

    def test_start(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities)

    def test_solo(self):
        exp_city = [('Chita', [1])]
        self.assertEqual(fit_transform('Chita'), exp_city)

    def test_double(self):
        exp_city = [
                       ('Chita', [1])
                   ] * 5
        self.assertEqual(fit_transform('Chita', 'Chita', 'Chita', 'Chita', 'Chita'), exp_city)


if __name__ == '__main__':
    unittest.main()
