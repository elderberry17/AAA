import pytest

from one_hot_encoder import fit_transform


def test_empty():
    with pytest.raises(TypeError):
        fit_transform()


def test_no():
    exp_city = []
    emp = []
    assert fit_transform(emp) == exp_city


def test_start():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_solo():
    assert fit_transform('Chita') == [('Chita', [1])]


def test_double():
    assert fit_transform('Chita', 'Chita', 'Chita', 'Chita', 'Chita') == [
        ('Chita', [1])
    ] * 5
