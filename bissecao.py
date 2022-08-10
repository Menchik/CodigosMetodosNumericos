import math as m

def func(x):
    return x**2-m.exp(-x)

def bissecao(a, b, erro):
    fa = func(a)

    if fa * func(b) >= 0:
        print("Dumbass")
        return

    c = a
    k = 0

    while b-a >= erro:
        k += 1  
        fc = func(c)
        c = (a+b)/2

        if fc == 0.0:
            break
        
        if fc * fa < 0:
            b = c
        else:
            a = c

    print(f"valor: {c:.4f}\niterações: {k}")

if __name__ == "__main__":
    a = 0
    b = 1
    erro = 0.01
    bissecao(a, b, erro)