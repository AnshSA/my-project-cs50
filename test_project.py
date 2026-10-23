
import pytest

from project import (
    calculate_strike_rate,
    calculate_batting_average,
    calculate_economy,
    calculate_bowling_average,
    calculate_bowling_strike_rate,
    calculate_fielding_contributions,
    calculate_fielding_success_rate,
)


def test_calculate_strike_rate():
    assert calculate_strike_rate(45, 30) == 150
    assert calculate_strike_rate(50, 10) == 500


def test_calculate_strike_rate_invalid():
    with pytest.raises(ValueError):
        calculate_strike_rate(100, 1)

    with pytest.raises(ValueError):
        calculate_strike_rate(50, 0)


def test_calculate_batting_average():
    assert calculate_batting_average(60, 2) == 30
    assert calculate_batting_average(50, 0) == 50


def test_calculate_economy():
    assert calculate_economy(24, 24) == 6


def test_calculate_bowling_average():
    assert calculate_bowling_average(24, 2) == 12
    assert calculate_bowling_average(24, 0) is None


def test_calculate_bowling_strike_rate():
    assert calculate_bowling_strike_rate(24, 2) == 12
    assert calculate_bowling_strike_rate(24, 0) is None


def test_calculate_fielding_contributions():
    assert calculate_fielding_contributions(4, 3, 3) == 10

    with pytest.raises(ValueError):
        calculate_fielding_contributions(5, 3, 3)


def test_calculate_fielding_success_rate():
    assert calculate_fielding_success_rate(4, 1, 0, 1) == pytest.approx(
        83.3333333333
    )

    assert calculate_fielding_success_rate(0, 0, 0, 0) is None

    with pytest.raises(ValueError):
        calculate_fielding_success_rate(5, 3, 3, 0)
