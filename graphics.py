import numpy as np
import matplotlib.pyplot as plt

GENERAL_PERIOD = 7 / 2
COSINE_PERIOD = 7
SINE_PERIOD = 7
LINE_STYLE = {
    "color": "black",
    "linestyle": "--",
    "linewidth": 0.8,
    "alpha": 0.35,
}

def value_label(value: float):
    if np.isclose(value, 0):
        return "0"
    if np.isclose(value, round(value)):
        return str(int(round(value)))
    numerator = int(round(2 * value))
    return rf"$\frac{{{numerator}}}{{2}}$"

def highlight_period(ax, n: int, period: float, start: float = 0.0):
    left = start + n * period
    right = start + (n + 1) * period
    color = "tab:blue" if n % 2 == 0 else "tab:orange"

    ax.axvspan(left, right, color=color, alpha=0.07, zorder=0)
    ax.axvline(left, **LINE_STYLE)

def draw_segments(ax, segments, shift: float = 0.0):
    for a, b, y in segments:
        ax.hlines(y, shift + a, shift + b, linewidth=2)

def draw_points(ax, points, shift: float = 0.0):
    for x0, y0 in points:
        ax.scatter(shift + x0, y0, s=35, zorder=3)

def setup_axes(ax, xlim, ylabel, title, ylim=(-0.5, 3.5)):
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("x")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

def draw_general_period(ax, n):
    shift = n * GENERAL_PERIOD

    intervals = [
        (0, 1, 0),
        (1, 2, 1),
        (2, 3, 2),
        (3, GENERAL_PERIOD, 3),
    ]

    points = [
        (0, 3/2),
        (1, 1/2),
        (2, 3/2),
        (3, 5/2),
        (GENERAL_PERIOD, 3/2),
    ]

    draw_segments(ax, intervals, shift)
    draw_points(ax, points, shift)

def draw_cosine_period(ax, n):
    shift = n * COSINE_PERIOD
    half_period = COSINE_PERIOD / 2

    intervals = [
        (-half_period, -3, 3),
        (-3, -2, 2),
        (-2, -1, 1),
        (-1, 1, 0),
        (1, 2, 1),
        (2, 3, 2),
        (3, half_period, 3),
    ]

    points = [
        (-3, 5/2),
        (-2, 3/2),
        (-1, 1/2),
        (1, 1/2),
        (2, 3/2),
        (3, 5/2),
    ]

    draw_segments(ax, intervals, shift)
    draw_points(ax, points, shift)

def draw_sine_period(ax, n):
    shift = n * SINE_PERIOD
    half_period = SINE_PERIOD / 2

    intervals = [
        (-half_period, -3, -3),
        (-3, -2, -2),
        (-2, -1, -1),
        (-1, 1, 0),
        (1, 2, 1),
        (2, 3, 2),
        (3, half_period, 3),
    ]

    points = [
        (-half_period, 0),
        (-3, -5/2),
        (-2, -3/2),
        (-1, -1/2),
        (1, 1/2),
        (2, 3/2),
        (3, 5/2),
        (half_period, 0),
    ]

    draw_segments(ax, intervals, shift)
    draw_points(ax, points, shift)

def plot_general_sum():
    _, ax = plt.subplots(figsize=(10, 4))

    for n in range(-2, 3):
        highlight_period(ax, n, period=GENERAL_PERIOD)
        draw_general_period(ax, n)

    ax.axvline(3 * GENERAL_PERIOD, **LINE_STYLE)

    period_ticks = np.arange(-2, 4) * GENERAL_PERIOD
    ax.set_xticks(period_ticks)
    ax.set_xticklabels([value_label(x) for x in period_ticks])

    setup_axes(
        ax,
        xlim=(-4, 8),
        ylabel="S(x)",
        title="Сумма общего тригонометрического ряда Фурье",
    )

def plot_cosine_sum():
    _, ax = plt.subplots(figsize=(10, 4))
    period_start = -COSINE_PERIOD / 2

    for n in range(-2, 3):
        highlight_period(ax, n, period=COSINE_PERIOD, start=period_start)
        draw_cosine_period(ax, n)

    ax.axvline(period_start + 3 * COSINE_PERIOD, **LINE_STYLE)

    period_ticks = period_start + np.arange(-1, 3) * COSINE_PERIOD
    ax.set_xticks(period_ticks)
    ax.set_xticklabels([value_label(x) for x in period_ticks])

    setup_axes(
        ax,
        xlim=(-11, 11),
        ylabel="$S_c(x)$",
        title="Сумма ряда Фурье по косинусам",
    )

def plot_sine_sum():
    _, ax = plt.subplots(figsize=(10, 4))
    period_start = -SINE_PERIOD / 2

    for n in range(-2, 3):
        highlight_period(ax, n, period=SINE_PERIOD, start=period_start)
        draw_sine_period(ax, n)

    ax.axvline(period_start + 3 * SINE_PERIOD, **LINE_STYLE)

    period_ticks = period_start + np.arange(-1, 3) * SINE_PERIOD
    ax.set_xticks(period_ticks)
    ax.set_xticklabels([value_label(x) for x in period_ticks])

    setup_axes(
        ax,
        xlim=(-11, 11),
        ylabel="$S_s(x)$",
        title="Сумма ряда Фурье по синусам",
        ylim=(-3.5, 3.5),
    )

def main():
    plot_general_sum()
    plot_cosine_sum()
    plot_sine_sum()
    plt.show()

if __name__ == "__main__":
    main()
