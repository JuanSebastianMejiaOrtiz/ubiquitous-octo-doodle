import sympy as sp
import numpy as np
import punto5


def routh(p):
    n = len(p) - 1  # degree of polynomial
    print("Degree of polynomial:", n)

    nfil = n + 1  # number of rows

    if n % 2 == 0:
        ncol = n // 2 + 1  # even degree
    else:
        ncol = (n + 1) // 2  # odd degree

    # Initialize first two rows
    M = np.zeros((nfil, ncol))

    if n % 2 == 0:
        m = n // 2 + 1
        M[1, m-1] = 0
    else:
        m = (n + 1) // 2
        M[1, m-1] = p[-1]

    for i in range(ncol):
        idx = 2 * i
        if idx < len(p):
            M[0, i] = p[idx]

    for i in range(ncol - 1):
        idx = 2 * i + 1
        if idx < len(p):
            M[1, i] = p[idx]

    # Calculate the rest of the rows
    for i in range(nfil - 2):
        for j in range(ncol):
            if j == ncol - 1:
                M[i+2, j] = 0
            else:
                if M[i+1, 0] != 0:
                    M[i+2, j] = (M[i+1, 0]*M[i, j+1] - M[i+1, j+1]*M[i, 0]) / M[i+1, 0]
                else:
                    M[i+2, j] = 0  # Avoid division by zero

    # Calculate the continuous fraction coefficients
    q = np.zeros(n)
    for i in range(n):
        if M[i+1, 0] != 0:
            q[i] = M[i, 0] / M[i+1, 0]
        else:
            q[i] = 0  # Again, avoid division by zero

    return M, q


s = sp.symbols('s')

H1_expanded = sp.expand(sp.denom(punto5.H1))
coeff = sp.Poly(H1_expanded, s)
coeff = coeff.all_coeffs()
print(routh(coeff))

H2_expanded = sp.expand(sp.denom(punto5.H2))
coeff = sp.Poly(H2_expanded, s)
coeff = coeff.all_coeffs()
print(routh(coeff))

H3_expanded = sp.expand(sp.denom(punto5.H3))
coeff = sp.Poly(H3_expanded, s)
coeff = coeff.all_coeffs()
print(routh(coeff))
