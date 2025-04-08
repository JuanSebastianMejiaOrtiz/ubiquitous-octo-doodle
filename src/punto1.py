import sympy as sp
import solEDOs

t = sp.symbols("t")
TFINAL = 10

y = sp.Function('y')
d1y = sp.diff(y(t), t)
d2y = sp.diff(y(t), t, 2)
d3y = sp.diff(y(t), t, 3)

# Primera Ecuacion Diferencial
c_is = {y(0): 0, d1y.subs(t, 0): 0}    #condiciones iniciales
x1 = sp.exp(-t/2) * sp.sin(2*sp.pi*t) + 2*sp.exp(-3*t)
stats = [
    {
        "title": "Solucion Ecuacion Dif. 1",
        "legend": r"$(D^2 + 3D + 2)y(t)$",
        "grid": True
    },
    {
        "title": "Entrada Ecuacion Dif. 1",
        "legend": r"$e^{-t/2} sin(2 \pi t) + 2e^{-3t}$",
        "grid": True
    }
]
eq = sp.Eq(d2y + 3*d1y + 2*y(t), x1)
solEDOs.solve(eq, x1, c_is, TFINAL, "t", stats)

# Segunda Ecuacion Diferencial
c_is = {y(0): 0, d1y.subs(t, 0): 0, d2y.subs(t, 0): 0}    #condiciones iniciales
x2 = 10*sp.Heaviside(t)
stats = [
    {
        "title": "Solucion Ecuacion Dif. 2",
        "legend": r"$(D^3 - 3D^2 + 7D - 5)y(t)$",
        "grid": True
    },
    {
        "title": "Entrada Ecuacion Dif. 2",
        "legend": r"$10 u(t)$",
        "grid": True
    }
]
eq = sp.Eq(d3y - 3*d2y + 7*d1y - 5*y(t), x2)
solEDOs.solve(eq, x2, c_is, TFINAL, "t", stats)

# Tercera Ecuacion Diferencial
c_is = {y(0): 0, d1y.subs(t, 0): 0}    #condiciones iniciales
x3 = 4 + 2*sp.exp(-3*t)
stats = [
    {
        "title": "Solucion Ecuacion Dif. 2",
        "legend": r"$(D^2 + 2D + 5)y(t)$",
        "grid": True
    },
    {
        "title": "Entrada Ecuacion Dif. 2",
        "legend": r"$4 + 2e^{-3t}$",
        "grid": True
    }
]
eq = sp.Eq(d2y + 2*d1y + 5*y(t), x3)
solEDOs.solve(eq, x3, c_is, TFINAL, "t", stats)
