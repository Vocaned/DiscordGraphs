import matplotlib.pyplot as plt
from typing import List

def multiplot(lines: tuple):
    fig, ax = plt.subplots()

    ymax = 0
    xmax = 0
    for xy in lines:
        ax.plot(xy[0], xy[1], color=xy[2], label=xy[3])
        xmax = max(len(xy[0]), xmax)
        ymax = max(max(xy[1]), ymax)

    plt.xticks(list(lines[0][0])[::xmax//10]) # TODO: Fix this shit
    plt.yticks(range(0, ymax+ymax//10, min(ymax, 2000)//4)) # TODO: Fix this shit
    plt.grid(b=True, which='major', color='#888888', linestyle='-', alpha=0.5)

    ax.legend()
    plt.show()

def lineplot(x: list, y: list, **kwargs):
    fig, ax = plt.subplots()

    ax.plot(x, y, **kwargs)

    xlen = len(x)
    ymax = max(y)
    plt.xticks(list(x)[::xlen//10]) # TODO: Fix this shit
    plt.yticks(range(0, ymax+ymax//10, min(ymax, 2000)//4)) # TODO: Fix this shit
    plt.grid(b=True, which='major', color='#888888', linestyle='-', alpha=0.5)

    ax.legend()
    plt.show()

def horizontalbar(x: list, y: list, xlabel: str, ylabel: str, title: str):
    fig, ax = plt.subplots()
    ax.barh(x, y, align='center')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.grid(axis='x')
    plt.show()