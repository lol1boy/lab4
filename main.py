import numpy
import math

def M(t):
    # function = pow(math.exp(50), -0.1*t) + 5*math.sin(t) 
    # # function = math.exp(50) ** (-0.1*t) + 5*math.sin(t)
    # return function
    return 50 * math.exp(-0.1 * t) + 5 * math.sin(t)

def M_analytical(t):
    return -5 * math.exp(-0.1 * t) + 5 * math.cos(t)

def M_numerical(t, h=0.001):
    return M(t + h) - M(t - h) / (2 * h)

def central_difference(t, h):
    """Basic numerical derivative with step h"""
    return (M(t + h) - M(t - h)) / (2 * h)

def runge_romberg(t, h):
    D_h   = central_difference(t, h)
    D_h2  = central_difference(t, h / 2)
    
    p = 2
    D = D_h2 + (D_h2 - D_h) / (2**p - 1)
    return D, D_h, D_h2

t0 = 1
h  = 0.01
exact = -5 * math.exp(-0.1 * t0) + 5 * math.cos(t0)

D, D_h, D_h2 = runge_romberg(t0, h)

print(f"D_h        = {D_h:.6f}")   # with step h
print(f"D_h/2      = {D_h2:.6f}")  # with step h/2
print(f"Runge-Romberg D = {D:.6f}")
print(f"Exact           = {exact:.6f}")
print(f"Error (RR)      = {abs(D - exact):.8f}")
print(f"Error (basic)   = {abs(D_h2 - exact):.8f}")
print("------------------------------")

print(f"Analytical : {M_analytical(t0):.6f}")
print(f"Numerical  : {M_numerical(t0):.6f}")

# print(M(1))
# print(M(2.5))