import numpy as np


def return1(E, E0, L, T, ik):
    return ((E - E0)/L*T + ik)

def return2(E, E0, L, T, ir, ik):
    return (-E0/L*T - (ir - ik)/(E - E0)*E + ir)

def border(E, E0, L, T, ir):
    return (ir - (E - E0)/L*T)


if __name__ == "__main__":
    with open("./SystemOptim/DownV/return.data", "w") as fp1:
        fp1.write("")
    fp1 = open("./SystemOptim/DownV/return.data", "a", encoding= "utf-8")
    if fp1 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/DownV/map.data", "w") as fp2:
        fp2.write("")
    fp2 = open("./SystemOptim/DownV/map.data", "a", encoding= "utf-8")
    if fp2 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/DownV/line.data", "w") as fp3:
        fp3.write("")
    fp3 = open("./SystemOptim/DownV/line.data", "a", encoding= "utf-8")
    if fp3 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/DownV/border.data", "w") as fp4:
        fp4.write("")
    fp4 = open("./SystemOptim/DownV/border.data", "a", encoding= "utf-8")
    if fp4 == None:print("FILE OPEN ERROR\n")

    max = 300
    write = 280

    f = 80.e3
    T = 1.0/f
    E = 50.0
    E0 = 13.7
    L = 1.e-3
    ir = 2.5

    D = border(E, E0, L, T, ir)
    print("%f %f" %(D, 0.0), file=fp4)
    print("%f %f" %(D, ir), file=fp4)

    Range_ik = np.arange(0, ir+1e-13, 0.01)
    for ik in Range_ik:
        if ik <= D:
            ik1 = return1(E, E0, L, T, ik)
        else:
            ik1 = return2(E, E0, L, T, ir, ik)
        print("%f %f" %(ik, ik1), file=fp1)
        print("%f %f" %(ik, ik), file=fp3)

    for count in range(max+1):
        if ik <= D:
            ik1 = return1(E, E0, L, T, ik)
        else:
            ik1 = return2(E, E0, L, T, ir, ik)

        if count >= write:
            print("%f %f" %(ik, ik1), file=fp2)
            ik = ik1
            print("%f %f" %(ik, ik1), file=fp2)
        else:
            ik = ik1

    fp1.close()
    fp2.close()
    fp3.close()
    fp4.close()