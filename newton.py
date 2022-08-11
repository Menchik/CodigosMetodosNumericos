import sympy as sp

def newton(f, a, erro, maxit):
    k = 1

    while k <= maxit:
        
        fa = f.subs(x, a)
        df = sp.diff(f, x)
        da = df.subs(x, a)
        c = a - fa/da

        if abs(c-a) < erro or abs(c-a)/abs(c) < erro or abs(f.subs(x, c)) < erro:
            print(f"valor: {c.evalf()}\niterações: {k}")
            return
        
        a = c

        k += 1
    print("Dumbass")

if __name__ == "__main__":
    x = sp.Symbol("x")
    f = x**2-sp.exp(-x)
    a = 0
    erro = 0.01
    maxit = 10
    newton(f, a, erro, maxit)