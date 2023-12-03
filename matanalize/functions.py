from math import exp
import numpy as np

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

def generate_bifurcation_data(x0: float) -> list[tuple[float, float]]:
    # config
    a_values = np.linspace(2.4, 4.0, 500)
    num_transient = 500
    num_points = 35

    data = []

    for a in a_values:
        x = x0
        for _ in range(num_transient):
            x = func(x, a)

        for _ in range(num_points):
            x = func(x, a)
            data.append((a, x))

    return np.array(data)