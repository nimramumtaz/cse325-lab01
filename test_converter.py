# CSE325-2026-L01-K7QX-T3
import pytest
from hand_written import celsius_to_fahrenheit as by_hand
from ai_assisted import celsius_to_fahrenheit as by_ai

RUN_PROFILE = "both-versions"


@pytest.mark.parametrize("fn", [by_hand, by_ai])
@pytest.mark.parametrize("c, f", [(100, 212), (0, 32), (-40, -40), (37, 98.6)])
def test_known_conversions(fn, c, f):
    assert fn(c) == pytest.approx(f)
