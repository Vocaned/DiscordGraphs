import numpy as np
import matplotlib.pyplot as plt
from typing import List
from utils import Line

def lineplot(*lines: plt.plot):
    fig, ax = plt.subplots()

    for line in lines:
        ax.plot(line.x, line.y, color=line.color, label=line.label, linestyle=line.linestyle, alpha=line.alpha) # There's gotta be a better way but I'm just too lazy

    plt.xticks(list(lines[0].x)[::15]) # TODO: Automatically calculate ticks to fit on screen
    plt.yticks(range(0, max(lines[0].y)+500, 500))

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