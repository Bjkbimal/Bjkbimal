"""Simple addition utility."""

from __future__ import annotations


def add_numbers(first: float, second: float) -> float:
    """Return the sum of *first* and *second*.

    Parameters
    ----------
    first: float
        The first addend.
    second: float
        The second addend.
    """

    return first + second


def _main() -> None:
    """Add two numbers provided by the user via standard input."""

    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
    except ValueError as exc:  # pragma: no cover - CLI only
        raise SystemExit(f"Invalid number provided: {exc}") from exc

    result = add_numbers(first, second)
    print(f"The sum of {first} and {second} is {result}.")


if __name__ == "__main__":  # pragma: no cover - CLI only
    _main()
