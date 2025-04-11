import sympy as sp
import solEDOs
import matplotlib.pyplot as plt


# Primera Ecuacion Diferencial
def firstEq(xIn, t, y, d1y, d2y):
    c_is = {y(0): 0, d1y.subs(t, 0): 0}
    stats = [
        {
            "title": "Ecuacion Dif. 1",
            "legend": r"$y(t)$",
            "grid": True,
            "xLabel": r"$t$",
        },
        {
            "title": "Ecuacion Dif. 1",
            "legend": r"$e^{-t/2} sin(2 \pi t) + 2e^{-3t}$",
            "grid": True,
            "xLabel": r"$t$",
        }
    ]
    eq = sp.Eq(d2y + 3*d1y + 2*y(t), xIn)
    solEDOs.solveAndPlot(eq, xIn, c_is, TFINAL, stats)
    return sp.dsolve(eq, ics=c_is)


# Segunda Ecuacion Diferencial
def secondEq(xIn, t, y, d1y, d2y, d3y):
    c_is = {y(0): 0, d1y.subs(t, 0): 0, d2y.subs(t, 0): 0}
    stats = [
        {
            "title": "Ecuacion Dif. 2",
            "legend": r"$y(t)$",
            "grid": True,
            "xLabel": r"$t$",
        },
        {
            "title": "Ecuacion Dif. 2",
            "legend": r"$10 u(t)$",
            "grid": True,
            "xLabel": r"$t$",
        }
    ]
    eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), xIn)
    solEDOs.solveAndPlot(eq, xIn, c_is, TFINAL, stats)
    return sp.dsolve(eq, ics=c_is)


# Tercera Ecuacion Diferencial
def thirdEq(xIn, t, y, d1y, d2y):
    c_is = {y(0): 0, d1y.subs(t, 0): 0}
    stats = [
        {
            "title": "Ecuacion Dif. 3",
            "legend": r"$y(t)$",
            "grid": True,
            "xLabel": r"$t$",
        },
        {
            "title": "Ecuacion Dif. 3",
            "legend": r"$4 + 2e^{-3t}$",
            "grid": True,
            "xLabel": r"$t$",
        }
    ]
    eq = sp.Eq(d2y + 2*d1y + 5*y(t), xIn)
    solEDOs.solveAndPlot(eq, xIn, c_is, TFINAL, stats)
    return sp.dsolve(eq, ics=c_is)


t = sp.symbols("t")
y = sp.Function('y')
d1y = sp.diff(y(t), t)
d2y = sp.diff(y(t), t, 2)
d3y = sp.diff(y(t), t, 3)

TFINAL = 10

x1 = sp.exp(-t/2) * sp.sin(2*sp.pi*t) + 2*sp.exp(-3*t)
x2 = 10*sp.Heaviside(t)
x3 = 4 + 2*sp.exp(-3*t)

sol1 = firstEq(x1, t, y, d1y, d2y)
sol2 = secondEq(x2, t, y, d1y, d2y, d3y)
sol3 = thirdEq(x3, t, y, d1y, d2y)
plt.show()

print("Solution 1:", sol1)
print("Solution 2:", sol2)
print("Solution 3:", sol3)
