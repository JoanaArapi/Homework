from functions import mean, median


def test_mean():
    assert mean([2, 3, 4, 5]) == 3.5


def test_median():
    assert median([2, 3, 4, 5, 6]) == 4
