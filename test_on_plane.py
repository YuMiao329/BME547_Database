import pytest


@pytest.mark.parametrize("input, expected", [
    ([(1, 10), (2, 20)], (10, 0)),
    ([(-2, 1), (-4, 2)], (-0.5, 0))])
def test_find_equation(input, expected):
    from on_plane import find_equation
    answer = find_equation(input)
    assert answer == expected


@pytest.mark.parametrize("input, expected", [
    ([20, 0, 7], 140),
    ([-5.8, 3.5, -0.3], 5.24)])
def test_find_point(input, expected):
    from on_plane import find_point
    answer = find_point(input[0], input[1], input[2])
    assert answer == expected


@pytest.mark.parametrize("input, expected", [
    ([[(1, 10), (2, 20)], 3], (3, 30)),
    ([[(-2, 1), (-4, 2)], -8], (-8, 4))])
def test_main(input, expected):
    from on_plane import main
    answer = main(input[0], input[1])
    assert answer == expected
