import numpy
import math

def speed_change(t):
    function = pow(math.exp(50), -0.1*t) + 5*math.sin(t) 
    # function = math.exp(50) ** (-0.1*t) + 5*math.sin(t)
    return function

print(speed_change(2.5))