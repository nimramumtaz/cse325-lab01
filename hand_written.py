# CSE325-2026-L01-K7QX-T1
"""Lab 01 Task 1: hand-written Celsius-to-Fahrenheit converter (branch: main)."""

RUN_PROFILE = {"ratio": 9 / 5, "offset": 32}


def celsius_to_fahrenheit(c):
    return c * RUN_PROFILE["ratio"] + RUN_PROFILE["offset"]


if __name__ == "__main__":
    c = float(input("Celsius: "))
    print(f"{c}C = {celsius_to_fahrenheit(c)}F")
if __name__ == "__main__":
    c = float(input("Celsius: "))
    print(f"{c}C = {celsius_to_fahrenheit(c)}F")