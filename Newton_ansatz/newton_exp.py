import numpy as np
import time


def iL0(Iph, vL, iL):
    #Iph = 1
    I0, gamma, Rs, Rsh, Te = 10e-11, 10, 0.1, 100, 300
    A = (1.6*10e-19) / (gamma*(1.38*10e-23)*Te)
    return Iph - I0*(np.exp(A*(vL + Rs*iL)) - 1) - (vL + iL*Rs)/Rsh - iL

def diL0(vL, iL):
    #Iph = 1
    I0, gamma, Rs, Rsh, Te = 10e-11, 10, 0.1, 100, 300
    A = (1.6*10e-19) / (gamma*(1.38*10e-23)*Te)
    return -I0*A*Rs*np.exp(A*(vL + Rs*iL)) - Rs/Rsh - 1

def newton_eta(iL):
    eta = 1e-6
    delta = 1e-8
    x = iL
    with open("./SystemOptim/Newton_ansatz/data_exp_eta.txt", "w") as f:
        f.write("")
    data = open("./SystemOptim/Newton_ansatz/data_exp_eta.txt", "a")

    for Iph in range(0, 21, 2):
        Iph = Iph*0.1
        for vL in range(0, 601, 1):
            vL = vL*0.01
            for i in range(100):
                a = (iL0(Iph, vL, x+eta) - iL0(Iph, vL, x)) / eta
                b = iL0(Iph, vL, x) - a*x
                x = -b / a

                if abs(iL0(Iph, vL, x)) < delta:
                    if x > 0:
                        print(f"Iph = {Iph}, vL = {vL}, iL = {x}", file=data)
                    break

    data.close()

def newton_dy(iL):
    eps = 1e-8
    x0 = iL
    x1 = x0
    with open("./SystemOptim/Newton_ansatz/data_exp_dy.txt", "w") as f:
        f.write("")
    data = open("./SystemOptim/Newton_ansatz/data_exp_dy.txt", "a")

    for Iph in range(0, 21, 2):
        Iph = Iph*0.1
        for vL in range(0, 601, 1):
            vL = vL*0.01
            for i in range(100):
                x1 = x0 - iL0(Iph, vL, x0)/diL0(vL, x0)
                delta = x0 - x1
                x0 = x1

                if abs(delta) < eps:
                    if x1 > 0:
                        print(f"Iph = {Iph}, vL = {vL}, iL = {x1}", file=data)
                    break

    data.close()


if __name__ == "__main__":
    start = time.perf_counter() # count program time

    iL = 1

    #newton_eta(iL)
    newton_dy(iL)

    print("program time =", time.perf_counter() - start)
    print("finish")

