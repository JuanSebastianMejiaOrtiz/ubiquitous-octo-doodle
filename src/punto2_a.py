import sympy as sp
import solEDOs
import matplotlib.pyplot as plt

t = sp.symbols("t")
y = sp.Function('y')
d1y = sp.diff(y(t), t)
d2y = sp.diff(y(t), t, 2)
d3y = sp.diff(y(t), t, 3)

TFINAL = 10

stats = [
    {
        "title": "Ecuacion Dif. 2",
        "legend": r"$y(t)$",
        "grid": True,
        "xLabel": r"$t$",
    },
    {
        "title": "Ecuacion Dif. 2",
        "legend": r"$2y(t)$",
        "grid": True,
        "xLabel": r"$t$",
    }
]

# Second LTI
c_is = {y(0): 0, d1y.subs(t, 0): 0, d2y.subs(t, 0): 0}
x1 = 10*sp.Heaviside(t)
x2 = 2*(10*sp.Heaviside(t))

plt.figure()

eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), x1)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[0])

eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), x2)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[1])

# Third LTI
c_is = {y(0): 0, d1y.subs(t, 0): 0}
x1 = 4 + 2*sp.exp(-3*t)
x2 = 2*(4 + 2*sp.exp(-3*t))

plt.figure()

stats[0]["title"] = "Ecuacion Dif. 3"
stats[1]["title"] = "Ecuacion Dif. 3"

eq = sp.Eq(d2y + 2*d1y + 5*y(t), x1)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[0])

eq = sp.Eq(d2y + 2*d1y + 5*y(t), x2)
sol = sp.dsolve(eq, ics=c_is)
solEDOs.plotDiff(sol, TFINAL, stats[1])
