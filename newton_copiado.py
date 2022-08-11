import math as m
# Python3 code for implementation of Newton
# Raphson Method for solving equations

# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func( x ):
	return x ** 2 - m.exp(-x)

# Derivative of the above function
# which is 3*x^x - 2*x
def derivFunc( x ):
	return 2 * x + m.exp(-x)

# Function to find the root
def newtonRaphson( x ):

    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x)/derivFunc(x)
        
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h

    print(f"The value of the root is : {x:.4f}")

# Driver program to test above
x0 = 200 # Initial values assumed
newtonRaphson(x0)

# This code is contributed by "Sharad_Bhardwaj"
