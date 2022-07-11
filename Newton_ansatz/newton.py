import numpy as np
import time

def y(E0, E):
    return 1 - E0/(E - E0)

def dy(E0, E):
    return E0/(E - E0)**2


def newton_eta(E0, E):
    eta = 1e-6
    delta = 1e-8
    x = E
    with open("./SystemOptim/Newton_ansatz/data_eta.txt", "w") as f:
        f.write("")
    data = open("./SystemOptim/Newton_ansatz/data_eta.txt", "a")

    for f in range(10, 100, 1):
        for i in range(100):
            a = (y(E0, x+eta) - y(E0, x)) / eta
            b = y(E0, x) - a*x
            x = -b / a

            if abs(y(E0, x)) < delta:
                print(f"f = {f}, E = {x}, AnsE = {2*E0}", file=data)
                break

    data.close()

def newton_dy(E0, E):
    eps = 1e-8
    x0 = E
    x1 = x0
    with open("./SystemOptim/Newton_ansatz/data_dy.txt", "w") as f:
        f.write("")
    data = open("./SystemOptim/Newton_ansatz/data_dy.txt", "a")

    for f in range(10, 100, 1):
        for i in range(100):
            x1 = x0 - y(E0, x0)/dy(E0, x0)
            delta = x0 - x1
            x0 = x1

            if abs(delta) < eps:
                print(f"f = {f}, E = {x1}, AnsE = {2*E0}", file=data)
                break

    data.close()


if __name__ == "__main__":
    start = time.perf_counter() # count program time

    E0 = 13.7
    E = 1.9 * E0

    #newton_eta(E0, E)
    newton_dy(E0, E)

    print("program time =", time.perf_counter() - start)
    print("finish")

