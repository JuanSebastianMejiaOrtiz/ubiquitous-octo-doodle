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
x1 = sp.exp(-t/2) * sp.sin(2*sp.pi*t)
stats = [
    {
        "title": "Solucion Ecuacion Dif. 1",
        "legend": r"$(D^2 + 3D + 2)y_1(t)$",
        "grid": True
    },
    {
        "title": "Entrada Ecuacion Dif. 1",
        "legend": r"$e^{-t/2} sin(2 \pi t)$",
        "grid": True
    }
]
eq = sp.Eq(d2y + 3*d1y + 2*y(t), x1)
solEDOs.solve(eq, x1, c_is, TFINAL, "t", stats)