import sympy as sp
import solEDOs
import matplotlib.pyplot as plt

t = sp.symbols("t")
y = sp.Function('y')
d1y = sp.diff(y(t), t)
d2y = sp.diff(y(t), t, 2)
d3y = sp.diff(y(t), t, 3)

TFINAL = 10

# First Differential Equation
c_is = {y(0): 0, d1y.subs(t, 0): 0}
x1 = sp.exp(-t/2) * sp.sin(2*sp.pi*t)
x2 = 2*sp.exp(-3*t)
x3 = x1 + x2

stats = [
    {
        "title": "Ecuacion Dif. 1",
        "legend": r"$y_1(t)$",
        "grid": True,
        "xLabel": r"$t$",
    },
    {
        "title": "Ecuacion Dif. 1",
        "legend": r"$y_2(t)$",
        "grid": True,
        "xLabel": r"$t$",
    },
    {
        "title": "Ecuacion Dif. 1",
        "legend": r"$y(t)$",
        "grid": True,
        "xLabel": r"$t$",
    },
]
eq = sp.Eq(d2y + 3*d1y + 2*y(t), x1)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[0])


eq = sp.Eq(d2y + 3*d1y + 2*y(t), x2)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[1])


eq = sp.Eq(d2y + 3*d1y + 2*y(t), x3)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[2])

plt.show()
