# 昇圧型コンバータ
import numpy as np


def SWon(E, L, i0, t):
    return (E*t/L + i0)

def SWoff(E, E0, L, ir, toff):
    return ((E - E0)*toff/L + ir)


if __name__ == "__main__":
    with open("./SystemOptim/UpV/sys1.data", "w") as fp1:
        fp1.write("")
    fp1 = open("./SystemOptim/UpV/sys1.data", "a", encoding= "utf-8")
    if fp1 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/UpV/sys2.data", "w") as fp2:
        fp2.write("")
    fp2 = open("./SystemOptim/UpV/sys2.data", "a", encoding= "utf-8")
    if fp2 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/UpV/clock.data", "w") as fp3:
        fp3.write("")
    fp3 = open("./SystemOptim/UpV/clock.data", "a", encoding= "utf-8")
    if fp3 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/UpV/ref.data", "w") as fp4:
        fp4.write("")
    fp4 = open("./SystemOptim/UpV/ref.data", "a", encoding= "utf-8")
    if fp4 == None:print("FILE OPEN ERROR\n")

    time = 0
    max = 300
    write = 280

    f = 30e3
    T = 1.0/f
    E = 25.0
    E0 = 48.0
    L = 1e-3
    i0 = 0.1
    ir = 2.5
    h = T/256

    sys = 1 # sys = 1 means switch is ON.

    for count in range(max+1):
        ton = L*(ir - i0)/E
        D = ir - E/L*T

        Range_t = np.arange(0, T+1e-13, h)
        for idx, t in enumerate(Range_t):
            if i0 <= D:
                #if t <= (T - 3*h):
                i = SWon(E, L, i0, t)
                #else:
                #    t = T
                #    i = SWon(E, L, i0, t)
                #    i0 = i
            else:
                if t <= ton:
                    i = SWon(E, L, i0, t)
                    sys = 1
                else:
                    toff = t - ton
                    i = SWoff(E, E0, L, ir, toff)
                    sys = 2

            if count >=  write:
                time += h
                print("%f %f" %(time, i))
                if sys == 1:
                    print("%.8f %f" %(time, i), file=fp1)
                else:
                    print("%.8f %f" %(time, i), file=fp2)
        
        i0 = i
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