import math as m

def func(x):
    return x**2-m.exp(-x)

def secante(a, b, erro, maxit):
    k = 1
    while k <= maxit:
        
        fa = func(a)
        fb = func(b)
        c = b - ((fb)*(b-a))/(fb-fa)

        if abs(c-b) < erro or abs(c-b)/abs(c) < erro or abs(func(c)) < erro:
            print(f"valor: {c:.4f}\niterações: {k}")
            return
        
        a = b
        b = c

        k += 1
    print("Dumbass")

if __name__ == "__main__":
    a = 0
    b = 1
    erro = 0.01
    maxit = 10
    secante(a, b, erro, maxit)