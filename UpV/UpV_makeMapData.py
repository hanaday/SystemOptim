import numpy as np


def return1(E, L, T, ik):
    return (E/L*T + ik)

def return2(E, E0, L, T, ir, ik):
    return ((E - E0)/L*T - (E - E0)*(ir - ik)/E + ir)

def border(E, L, T, ir):
    return (ir - E/L*T)


if __name__ == "__main__":
    max = 300
    write = 280

    with open("./SystemOptim/UpV/return.data", "w") as fp1:
        fp1.write("")
    fp1 = open("./SystemOptim/UpV/return.data", "a", encoding= "utf-8")
    if fp1 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/UpV/map.data", "w") as fp2:
        fp2.write("")
    fp2 = open("./SystemOptim/UpV/map.data", "a", encoding= "utf-8")
    if fp2 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/UpV/line.data", "w") as fp3:
        fp3.write("")
    fp3 = open("./SystemOptim/UpV/line.data", "a", encoding= "utf-8")
    if fp3 == None:print("FILE OPEN ERROR\n")
    with open("./SystemOptim/UpV/border.data", "w") as fp4:
        fp4.write("")
    fp4 = open("./SystemOptim/UpV/border.data", "a", encoding= "utf-8")
    if fp4 == None:print("FILE OPEN ERROR\n")

    f = 30.e3
    T = 1.0/f
    E = 24.0
    E0 = 48.0
    L = 1.e-3
    ir = 2.5

    D = border(E, L, T, ir)
    print("%f %f" %(D, 0.0), file=fp4)
    print("%f %f" %(D, ir), file=fp4)

    Range_ik = np.arange(0, ir+1e-13, 0.01)
    for ik in Range_ik:
        if ik <= D:
            ik1 = return1(E, L, T, ik)
        else:
            ik1 = return2(E, E0, L, T, ir, ik)
        print("%f %f" %(ik, ik1), file=fp1)
        print("%f %f" %(ik, ik), file=fp3)

    for count in range(max+1):
        if ik <= D:
            ik1 = return1(E, L, T, ik)
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
