import sympy as sp
import numpy as np
import solEDOs
import matplotlib.pyplot as plt


# First Differential Equation
def firstEq(xIn, t, y, d1y, d2y):
    c_is = {y(0): 0, d1y.subs(t, 0): 0}
    stats = [
        {
            "title": "Ecuacion Dif. 1",
            "legend": r"$y(t)$",
            "grid": True,
            "xLabel": r"$t$",
        },
    ]
    eq = sp.Eq(d2y + 3*d1y + 2*y(t), xIn)
    sol = sp.dsolve(eq, ics=c_is)
    plt.figure()
    solEDOs.plotDiff(sol, TFINAL, stats[0])
    return sol


# Second Differential Equation
def secondEq(xIn, t, y, d1y, d2y, d3y):
    c_is = {y(0): 0, d1y.subs(t, 0): 0, d2y.subs(t, 0): 0}
    stats = [
        {
            "title": "Ecuacion Dif. 2",
            "legend": r"$y(t)$",
            "grid": True,
            "xLabel": r"$t$",
        },
    ]
    eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), xIn)
    sol = sp.dsolve(eq, ics=c_is)
    plt.figure()
    solEDOs.plotDiff(sol, TFINAL, stats[0])
    return sol


# Third Differential Equation
def thirdEq(xIn, t, y, d1y, d2y):
    c_is = {y(0): 0, d1y.subs(t, 0): 0}
    stats = [
        {
            "title": "Ecuacion Dif. 3",
            "legend": r"$y(t)$",
            "grid": True,
            "xLabel": r"$t$",
        },
    ]
    eq = sp.Eq(d2y + 2*d1y + 5*y(t), xIn)
    sol = sp.dsolve(eq, ics=c_is)
    plt.figure()
    solEDOs.plotDiff(sol, TFINAL, stats[0])
    return sol


def delta(t, a=0.05):
    return np.exp(-(t/a)**2) / (np.fabs(a) * np.sqrt(np.pi))


t = sp.symbols("t")
y = sp.Function('y')
d1y = sp.diff(y(t), t)
d2y = sp.diff(y(t), t, 2)
d3y = sp.diff(y(t), t, 3)

TFINAL = 10
x = sp.DiracDelta(t)

natSol1 = firstEq(x, t, y, d1y, d2y)
natSol2 = secondEq(x, t, y, d1y, d2y, d3y)
natSol3 = thirdEq(x, t, y, d1y, d2y)
plt.show()
