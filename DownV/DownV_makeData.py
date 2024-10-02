# 降圧型コンバータ
import numpy as np


def SWon(E, E0, L, ik, t):
    return ((E - E0)/L*t + ik)

def SWoff(E0, L, ir, t):
    return (-E0/L*t + ir)

def border(E, E0, L, T, ir):
    return (ir - (E - E0)/L*T)

def t_on(E, E0, L, ir, ik):
    return (L*(ir - ik)/(E - E0))


if __name__ == "__main__":
    with open("./SystemOptim/DownV/sys1.data", "w") as fp1:
        fp1.write("")
    fp1 = open("./SystemOptim/DownV/sys1.data", "a", encoding= "utf-8")
    if fp1 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/DownV/sys2.data", "w") as fp2:
        fp2.write("")
    fp2 = open("./SystemOptim/DownV/sys2.data", "a", encoding= "utf-8")
    if fp2 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/DownV/clock.data", "w") as fp3:
        fp3.write("")
    fp3 = open("./SystemOptim/DownV/clock.data", "a", encoding= "utf-8")
    if fp3 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/DownV/ref.data", "w") as fp4:
        fp4.write("")
    fp4 = open("./SystemOptim/DownV/ref.data", "a", encoding= "utf-8")
    if fp4 == None:print("FILE OPEN ERROR\n")

    time = 0
    max = 300
    write = 280

    f = 80e3
    T = 1.0/f
    E = 50.0
    E0 = 13.7
    L = 1e-3
    ik = 0
    ir = 2.5
    h = T/256

    sys = 1 # sys = 1 means switch is ON.

    for count in range(max+1):
        ton = t_on(E, E0, L, ir, ik)
        D = border(E, E0, L, T, ir)

        Range_t = np.arange(0, T+h, h)
        for idx, t in enumerate(Range_t):
            if ik <= D:
                ik1 = SWon(E, E0, L, ik, t)
            else:
                if t <= ton:
                    ik1 = SWon(E, E0, L, ik, t)
                    sys = 1
                else:
                    toff = t - ton
                    ik1 = SWoff(E0, L, ir, toff)
                    sys = 2

            if count >=  write:
                time += h
                print("%f %f" %(time, ik1))
                if sys == 1:
                    print("%.8f %f" %(time, ik1), file=fp1)
                else:
                    print("%.8f %f" %(time, ik1), file=fp2)
        
        ik = ik1
        sys = 1

        if count >= write:
            Range_clk = np.arange(0, 3+1e-13, 5e-3)
            for clk in Range_clk:
                print("%f %f" %(time, clk), file=fp3)
                print("%f %f" %(time, ir), file=fp4)

    fp1.close()
    fp2.close()
    fp3.close()
    fp4.close()

    print("finish")