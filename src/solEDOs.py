import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# Agarra la solución de la ecuación diferencial y la grafica
def plotDiff(sol, timeSol, stats, SYMBOL="t"):
    t = sp.symbols(SYMBOL)
    func = sp.lambdify(t, sol.rhs, 'numpy')
    plot(func, timeSol, stats)


# Grafica una funcion que se le ingrese
def plot(func, timeSol, stats):
    xVals = np.linspace(0, timeSol, 1000)
    yVals = func(xVals)
    plt.plot(xVals, yVals, label=stats["legend"])
    if stats["title"]:
        plt.title(stats["title"])
    if stats["legend"]:
        plt.legend()
    if stats["xLabel"]:
        plt.xlabel(stats["xLabel"])
    if stats["grid"]:
        plt.grid(stats["grid"])


# Agarra la ecuación diferencial, la soluciona y la grafica
def solveAndPlot(eq, xIn, c_is, TFINAL, stats, SYMBOL="t"):
    sol = sp.dsolve(eq, ics=c_is)
    plt.figure()
    plotDiff(sol, TFINAL, stats[0])
    plot(sp.lambdify(SYMBOL, xIn, "numpy"), TFINAL, stats[1])
