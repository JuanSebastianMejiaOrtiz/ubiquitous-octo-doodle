import sympy as sp
import matplotlib.pyplot as plt
import solEDOs
import punto3


def plotConvolution(xIn, natSol, TFINAL, SYMBOL="t"):
    t = sp.symbols(SYMBOL, positive=True)
    tau = sp.symbols(r'\tau', positive=True)
    h = natSol.rhs.subs(t, t - tau)
    x_tau = xIn.subs(t, tau)
    sol = sp.integrate(x_tau * h, (tau, 0, t))
    stats = {
        "title": "Convolution Integral Solution",
        "legend": r"$y(t)$",
        "grid": True,
        "xLabel": r"$t$",
    }
    solEDOs.plot(sp.lambdify(SYMBOL, sol, "numpy"), TFINAL, stats)
    return sp.simplify(sol)


t = sp.symbols("t")
TFINAL = 10

x1 = sp.exp(-t/2) * sp.sin(2*sp.pi*t) + 2*sp.exp(-3*t)
x2 = 10*sp.Heaviside(t)
x3 = 4 + 2*sp.exp(-3*t)

conv1 = plotConvolution(x1, punto3.natSol1, TFINAL)
plt.show()
conv2 = plotConvolution(x2, punto3.natSol2, TFINAL)
plt.show()
conv3 = plotConvolution(x3, punto3.natSol3, TFINAL)
plt.show()

print("Convolution Solution 1:", conv1)
print("Convolution Solution 2:", conv2)
print("Convolution Solution 3:", conv3)
