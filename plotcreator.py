import numpy as np
import matplotlib.pyplot as plt
from typing import List
from utils import Line

def lineplot(x: list, y: list, **kwargs):
    fig, ax = plt.subplots()

    ax.plot(x, y, **kwargs)

    xlen = len(x)
    ymax = max(y)
    plt.xticks(list(x)[::xlen//5])
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