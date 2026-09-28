# CSE325-2026-L01-K7QX-T2
"""Lab 01 Task 2: AI-assisted Celsius-to-Fahrenheit converter (branch: ai-build)."""

RUN_PROFILE = {"ratio": 9 / 5, "offset": 32}


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return celsius * RUN_PROFILE["ratio"] + RUN_PROFILE["offset"]


def parse_input(text: str):
    """Return a list of Celsius values, or None if the input is invalid.

    Accepts either one number ("36.6") or a range "start stop step" ("0 100 20").
    """
    try:
        numbers = [float(part) for part in text.split()]
    except ValueError:
        return None

    if len(numbers) == 1:
        return numbers
    if len(numbers) == 3:
        start, stop, step = numbers
        if step <= 0 or start > stop:
            return None
        count = int((stop - start) // step) + 1
        return [start + i * step for i in range(count)]
    return None


def main() -> None:
    while True:
        text = input("Celsius (one value, or 'start stop step'): ")
        values = parse_input(text)
        if values is not None:
            break
        print("Invalid input. Example: 36.6  or  0 100 20")

    for celsius in values:
        print(f"{celsius}C = {celsius_to_fahrenheit(celsius)}F")


if __name__ == "__main__":
    main()