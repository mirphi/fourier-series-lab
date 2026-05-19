import matplotlib.pyplot as plt
import numpy as np

GENERAL_PERIOD = 7 / 2
TRIG_PERIOD = 7
N_VALUES = (3, 10, 30)

def value_label(value: float) -> str:
    if np.isclose(value, 0):
        return "0"
    if np.isclose(value, round(value)):
        return str(int(round(value)))
    numerator = int(round(2 * value))
    return rf"$\frac{{{numerator}}}{{2}}$"

def setup_axes(ax, xlim, ylim, ylabel: str, title: str) -> None:
    ax.axhline(0, linewidth=0.8, color="black")
    ax.axvline(0, linewidth=0.8, color="black")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

def general_a(k):
    return (
        -np.sin(np.pi * k / 7)
        + np.sin(3 * np.pi * k / 7)
        - np.sin(5 * np.pi * k / 7)
    ) / (np.pi * k)

def general_b(k):
    return (
        np.cos(np.pi * k / 7)
        + np.cos(3 * np.pi * k / 7)
        + np.cos(5 * np.pi * k / 7)
        - 3 * (-1) ** k
    ) / (np.pi * k)

def cosine_a(k):
    return (
        -2
        / (np.pi * k)
        * (
            np.sin(2 * np.pi * k / 7)
            + np.sin(4 * np.pi * k / 7)
            + np.sin(6 * np.pi * k / 7)
        )
    )

def sine_b(k):
    return (
        2
        / (np.pi * k)
        * (
            np.cos(2 * np.pi * k / 7)
            + np.cos(4 * np.pi * k / 7)
            + np.cos(6 * np.pi * k / 7)
            - 3 * (-1) ** k
        )
    )

def partial_general_sum(x, n: int):
    result = np.full_like(x, 9 / 7, dtype=float)

    for k in range(1, n + 1):
        angle = 4 * np.pi * k * (x - 7 / 4) / 7
        result += general_a(k) * np.cos(angle) + general_b(k) * np.sin(angle)

    return result

def partial_cosine_sum(x, n: int):
    result = np.full_like(x, 9 / 7, dtype=float)

    for k in range(1, n + 1):
        result += cosine_a(k) * np.cos(2 * np.pi * k * x / 7)

    return result

def partial_sine_sum(x, n: int):
    result = np.zeros_like(x, dtype=float)

    for k in range(1, n + 1):
        result += sine_b(k) * np.sin(2 * np.pi * k * x / 7)

    return result

def plot_partial_sums(
    x, partial_sum,
    xlim, ylim, xticks, ylabel: str, title: str,
) -> None:
    fig, axes = plt.subplots(len(N_VALUES), 1, figsize=(10, 8), sharex=True)
    visible_ticks = [tick for tick in xticks if xlim[0] <= tick <= xlim[1]]

    for ax, n in zip(axes, N_VALUES):
        ax.plot(x, partial_sum(x, n), linewidth=1.5, color="tab:blue")
        setup_axes(ax, xlim=xlim, ylim=ylim, ylabel=ylabel, title=f"{title}, N={n}")

    axes[-1].set_xlabel("x")
    axes[-1].set_xticks(visible_ticks)
    axes[-1].set_xticklabels([value_label(tick) for tick in visible_ticks])
    axes[-1].set_xlim(*xlim)

    fig.tight_layout()

def plot_general_partial_sums() -> None:
    xlim = (-4, 8)
    x = np.linspace(*xlim, 4000)
    xticks = np.arange(-2, 4) * GENERAL_PERIOD

    plot_partial_sums(
        x=x,
        partial_sum=partial_general_sum,
        xlim=xlim,
        ylim=(-1, 4),
        xticks=xticks,
        ylabel="$S_N(x)$",
        title="Частичная сумма общего тригонометрического ряда",
    )

def plot_cosine_partial_sums() -> None:
    xlim = (-11, 11)
    x = np.linspace(*xlim, 5000)
    period_start = -TRIG_PERIOD / 2
    xticks = period_start + np.arange(-1, 3) * TRIG_PERIOD

    plot_partial_sums(
        x=x,
        partial_sum=partial_cosine_sum,
        xlim=xlim,
        ylim=(-1, 4),
        xticks=xticks,
        ylabel="$S_{c,N}(x)$",
        title="Частичная сумма ряда Фурье по косинусам",
    )

def plot_sine_partial_sums() -> None:
    xlim = (-11, 11)
    x = np.linspace(*xlim, 5000)
    period_start = -TRIG_PERIOD / 2
    xticks = period_start + np.arange(-1, 3) * TRIG_PERIOD

    plot_partial_sums(
        x=x,
        partial_sum=partial_sine_sum,
        xlim=xlim,
        ylim=(-4, 4),
        xticks=xticks,
        ylabel="$S_{s,N}(x)$",
        title="Частичная сумма ряда Фурье по синусам",
    )

def main():
    plot_general_partial_sums()
    plot_cosine_partial_sums()
    plot_sine_partial_sums()
    plt.show()

if __name__ == "__main__":
    main()
