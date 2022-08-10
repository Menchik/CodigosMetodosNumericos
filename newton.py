import math as m
import sympy as sp

def newton(a, erro, maxit):
    k = 1
    x = sp.symbols("x")
    f = x**2-sp.exp(-x)

    while k <= maxit:
        
        fa = f.subs(x, a)
        df = sp.diff(f, x)
        c = a - fa/df.subs(x, a)
        print(c)

        if abs(c-a) < erro or abs(c-a)/abs(c) < erro or abs(f.subs(x, c)) < erro:
            print(f"valor: {c}\niterações: {k}")
            return
        
        a = c

        k += 1
    print("Dumbass")

if __name__ == "__main__":
    a = 0
    erro = 0.01
    maxit = 10
    newton(a, erro, maxit)