# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 16:33:03 2025

@author: USUARIO
"""
import sympy as sp
import solEDOs
import matplotlib.pyplot as plt

t = sp.symbols("t")
TFINAL = 10

y = sp.Function('y')
d1y = sp.diff(y(t), t)
d2y = sp.diff(y(t), t, 2)
d3y = sp.diff(y(t), t, 3)

stats = [
    {
        "title": "Ecuacion Dif. 2",
        "legend": r"$y_1(t)$",
        "grid": True,
        "xLabel": r"$t$",
    },
    {
        "title": "Ecuacion Dif. 2",
        "legend": r"$2y_1(t)$",
        "grid": True,
        "xLabel": r"$t$",
    }
]


#SEGUNDO SLIT
c_is = {y(0): 0, d1y.subs(t, 0): 0, d2y.subs(t, 0): 0} #condiciones iniciales
x1 = 10*sp.Heaviside(t)
x2 = 2*(10*sp.Heaviside(t))

plt.figure()

eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), x1)
sol = sp.dsolve(eq, ics=c_is) 
solEDOs.plotDiff(sol, TFINAL, stats[0])

eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), x2)
sol = sp.dsolve(eq, ics=c_is) 
solEDOs.plotDiff(sol, TFINAL, stats[1])

#TERCER SLIT
c_is = {y(0): 0, d1y.subs(t, 0): 0}    #condiciones iniciales
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




