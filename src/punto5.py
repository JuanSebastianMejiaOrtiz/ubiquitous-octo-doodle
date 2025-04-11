import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import punto3

t, s = sp.symbols('t s')

def get_poles_zeros(H):
    numer = sp.numer(H)  
    denom = sp.denom(H)  
    zeros = sp.solve(numer, s)  
    poles = sp.solve(denom, s)  
    return zeros, poles

h1 = punto3.natSol1.rhs
h2 = punto3.natSol2.rhs
h3 = punto3.natSol3.rhs

# Laplace transform
H1 = sp.laplace_transform(h1, t, s, noconds=True)
H1 = sp.simplify(H1)

H2 = sp.laplace_transform(h2, t, s, noconds=True)
H2 = sp.simplify(H2)

H3 = sp.laplace_transform(h3, t, s, noconds=True)
H3 = sp.simplify(H3)

zeros_H1, poles_H1 = get_poles_zeros(H1)

zeros_H2, poles_H2 = get_poles_zeros(H2)

zeros_H3, poles_H3 = get_poles_zeros(H3)


def plot_poles_zeros(zeros_numeric, poles_numeric, title):
    plt.figure()
    poles = [complex(p.evalf()) for p in poles_numeric]
    zeros = [complex(z.evalf()) for z in zeros_numeric]

    plt.scatter(np.real(poles), np.imag(poles),
                marker='x', color='r', label='Poles')
    plt.scatter(np.real(zeros), np.imag(zeros),
                marker='o', color='b', label='Zeros')
    plt.axhline(0, color='k', linestyle='--')
    plt.axvline(0, color='k', linestyle='--')
    plt.xlabel('Re(s)')
    plt.ylabel('Im(s)')
    plt.title(title)
    plt.grid()
    plt.legend()


zeros_H1, poles_H1 = get_poles_zeros(H1)
plot_poles_zeros(zeros_H1, poles_H1, "Pole-Zero Plot: System 1")

zeros_H2, poles_H2 = get_poles_zeros(H2)
plot_poles_zeros(zeros_H2, poles_H2, "Pole-Zero Plot: System 2")

zeros_H3, poles_H3 = get_poles_zeros(H3)
plot_poles_zeros(zeros_H3, poles_H3, "Pole-Zero Plot: System 3")

plt.show()
