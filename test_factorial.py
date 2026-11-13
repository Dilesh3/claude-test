import math
import subprocess
import sys
from pathlib import Path

import pytest

from factorial import factorial

SCRIPT = Path(__file__).parent / "factorial.py"


@pytest.mark.parametrize(
    "n, expected",
    [(0, 1), (1, 1), (2, 2), (3, 6), (5, 120), (10, 3628800)],
)
def test_known_values(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("n", range(0, 30))
def test_matches_math_factorial(n):
    assert factorial(n) == math.factorial(n)


def test_large_number():
    assert factorial(100) == math.factorial(100)


def test_recurrence():
    for n in range(1, 50):
        assert factorial(n) == n * factorial(n - 1)


@pytest.mark.parametrize("n", [-1, -5, -100])
def test_negative_raises(n):
    with pytest.raises(ValueError, match="negative"):
        factorial(n)


def run_script(stdin):
    return subprocess.run(
        [sys.executable, str(SCRIPT)], input=stdin, capture_output=True, text=True
    ).stdout


def test_cli_valid_input():
    assert "5! = 120" in run_script("5\n")


def test_cli_negative_input():
    assert "Error: factorial is not defined for negative numbers" in run_script("-3\n")


def test_cli_non_integer_input():
    assert "Error:" in run_script("abc\n")
