import math
def metodo_biseccion(func, a, b, error_aceptado):
  

    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)

    while error > error_aceptado:
        c = (b + a) / 2


        if f(a) * f(b) >= 0:
            print("no se puede garantizar la existencia de una raiz en el intervalo")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b-a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b-a)

        else:
            print("algo salió mal")
            quit()

    print(f"el error es {error}")
    print(f"la frontera inferior, a, es {a} y la frontera superior, b, es {b} ")

#metodo_biseccion("(4*x ** 3) + 3*x -3", 0, 1, 0.05)
metodo_biseccion("math.exp(3*x) - 4", 0, 1, 0.01)

#metodo_biseccion("(3*x ** 2)-4", -2, 0, 0.05)