import matplotlib.pyplot as plt


def return1(E, E0, L, T, ik):
    return ((E - E0)/L*T + ik)

def return2(E, E0, L, toff, ir, ik):
    return (-E0/L*toff - (ir - ik)/(E - E0)*L + ir)

def border(E, E0, L, T, ir):
    return (ir - (E - E0)/L*T)

def t_on(E, E0, L, ir, ik):
    return (L*(ir - ik)/(E - E0))


if __name__ == "__main__":
    with open("./SystemOptim/DownV_brute/1para.data", "w") as f:
        f.write("")
    fp1 = open("./SystemOptim/DownV_brute/1para.data", "a")
    with open("./SystemOptim/DownV_brute/border.data", "w") as f:
        f.write("")
    fp2 = open("./SystemOptim/DownV_brute/border.data", "a")

    cmax = 500
    wcount = 490
    E0 = 13.7
    L = 1.e-3
    f = 80e3
    ir = 2.5
    ik = 0
    eps = 1e-6
    #f_start, f_end, f_step = 10e3, 100e3, 1e3 # [Hz]
    E_start, E_end, E_step = 20, 100, 0.1 # [V]

    #f_roof = int((f_end - f_start)/f_step)
    #E_roof = int((E_end - E_start)/E_step)

    E_list, ik_list = [], []
    for E in range(int(E_start/E_step), int(E_end/E_step)+1, 1):
        T = 1/f
        E = E * E_step
        D = border(E, E0, L, T, ir)

        for count in range(cmax):
            ton = t_on(E, E0, L, ir, ik)
            toff = T - ton

            if ik <= D:
                ik1 = return1(E, E0, L, T, ik)
            else:
                ik1 = return2(E, E0, L, toff, ir, ik)

            if count > wcount:
                E_list.append(E)
                ik_list.append(ik)

                print(f"E = {E}, ik = {ik}", file=fp1)
                print(f"E = {E}, D = {D}", file=fp2)
            ik = ik1

    plt.xlabel("E [V]")
    plt.ylabel("$i_{k}$ [A]")
    plt.scatter(E_list, ik_list, s=1)
    plt.savefig(f"./SystemOptim/DownV_brute/1para_graph.jpg")

    fp1.close()
    fp2.close()