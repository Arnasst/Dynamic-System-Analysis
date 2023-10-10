from math import exp

MAX_POINTS = 200


def func(x: float, a: float) -> float:
    return x * exp(a*(1 - x))


def calculate_time_series(x0: float, a: float) -> list[tuple[int, float]]:
    values = [(0, x0)]
    for i in range(1, MAX_POINTS):
        last_y = values[i-1][1]
        y = func(last_y, a)
        values.append((i, y))
    return values


def calculate_iterative_series(x0: float, a: float) -> list[tuple[float, float]]:
    last_x = x0
    values = [(x0, 0)]
    for i in range(1, MAX_POINTS):
        y = func(last_x, a)
        values.append((last_x, y))
        values.append((y, y))
        last_x = y
    return values
