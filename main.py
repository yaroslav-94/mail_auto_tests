import pytest

t_data = [
    ((1, 2, 3), (1, 2, 4), (1, 2, 3, 1, 2, 4)),
    ((1,), ("2",), (1, "2"))
]

f_data = [
    (1, 10.0, 11.0),
    (0.9, -0.5, 0.4),
    (float("123"), 123, 246)
]


def test_tuple_1():
    try:
        assert (1,) + "2"
    except TypeError:
        pass


@pytest.mark.parametrize("a, b, param", t_data)
def test_tuple_2(a, b, param):
    c = a + b
    assert c == param


def test_tuple_3():
    assert tuple("qwerty") == ("q", "w", "e", "r", "t", "y")


def test_float_1():
    try:
        assert float("123_")
    except ValueError:
        pass


@pytest.mark.parametrize("a, b, param", f_data)
def test_float_2(a, b, param):
    assert a+b == param


def test_float_3():
    assert float("123.0") == 123.0
