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
    return (M(t + h) - M(t - h)) / (2 * h)

def central_difference(t, h):
    """Basic numerical derivative with step h"""
    return (M(t + h) - M(t - h)) / (2 * h)

def runge_romberg(t, h):
    D_h   = central_difference(t, h)
    D_h2  = central_difference(t, h / 2)
    D_h4 = central_difference(t, h / 4)

    p = 2
    D = D_h2 + (D_h2 - D_h) / (2**p - 1)
    return D, D_h, D_h2, D_h4

def aitken_method(t, h):
    d_h  = (M(t + h) - M(t - h)) / (2 * h)
    d_2h = (M(t + 2*h) - M(t - 2*h)) / (4 * h)
    d_4h = (M(t + 4*h) - M(t - 4*h)) / (8 * h)

    numerator = (d_2h**2) - (d_4h * d_h)
    denominator = 2*d_2h - (d_4h + d_h)
    
    refined_val = numerator / denominator

    p_estimate = (1 / math.log(2)) * math.log(abs((d_4h - d_2h) / (d_2h - d_h)))

    return refined_val, p_estimate, d_h, d_2h, d_4h

t0 = 1
h  = 0.01
h_initial = 0.001
exact = -5 * math.exp(-0.1 * t0) + 5 * math.cos(t0)
refined_aitken, p_val, d_h, d_2h, d_4h = aitken_method(t0, h_initial)
ы
D, D_h, D_h2, D_h4 = runge_romberg(t0, h)ы

print(f"D_h        = {D_h:.6f}")
print(f"D_h/2      = {D_h2:.6f}")
print(f"D_h/4      = {D_h4:.6f}")
print(f"Runge-Romberg D = {D:.6f}")
print(f"Exact           = {exact:.6f}")
print(f"Error (RR)      = {abs(D - exact):.8f}")
print(f"Error (basic)   = {abs(D_h2 - exact):.8f}")
print("------------------------------")

print(f"Analytical : {M_analytical(t0):.6f}")
print(f"Numerical  : {M_numerical(t0):.6f}")

print("------------------------------")

print(f"Aitken Refined Value: {refined_aitken:.10f}")
print(f"Estimated Order (p): {p_val:.4f}")
print(f"Error vs Analytical: {abs(refined_aitken - exact):.12f}")

# print(M(1))
# print(M(2.5))