import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def plotDiff(sol, timeSol, stats):
    t = sp.symbols("t")
    func = sp.lambdify(t, sol.rhs, 'numpy')
    plot(func, timeSol, stats)

def plot(func, timeSol, stats):
    xVals = np.linspace(0, timeSol, 1000)
    yVals = func(xVals)
    plt.figure(figsize=(10,5))
    plt.plot(xVals, yVals, label=stats["legend"])
    plt.title(stats["title"])
    if stats["legend"]:  # Only show legend if it's not empty
        plt.legend()
    plt.grid(stats["grid"])

def solve(eq, xIn, c_is, TFINAL, SYMBOL, stats):
    sol = sp.dsolve(eq, ics=c_is)
    plotDiff(sol, TFINAL, stats[0])
    plot(sp.lambdify(SYMBOL, xIn, "numpy"), TFINAL, stats[1])