from hypothesis import given, strategies

from jaro import jaro


def test_add_integers():
    assert jaro.add(1, 1) == 2


@given(strategies.integers())
def test_add_same_integers(i):
    assert jaro.add(i, i) == i * 2
