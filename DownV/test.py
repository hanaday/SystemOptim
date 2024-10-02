import matplotlib.pyplot as plt
import numpy as np


def SWon(E, E0, L, ik, t):
    return ((E - E0)/L*t + ik)

def SWoff(E0, L, ir, toff):
    return (-E0*toff/L + ir)

def border(E, E0, L, T, ir):
    return (ir - (E - E0)/L*T)

def t_on(E, E0, L, ir, ik):
    return (L*(ir - ik)/(E - E0))

time = 0
max = 300
write = 280
f = 80e3
T = 1.0/f
E = 50.0
E0 = 13.7
L = 1e-3
ik = 0
ir = 3.0
h = T/256

i_list = np.array([]) #list
ir_list = np.array([]) #list
clk_list = np.array([]) #list




sys = 1 #SW is ON

for count in np.arange(max+1):
    ton = L*(ir - ik)/(E - E0)
    D = ir - (E - E0)/L*T

    
    for t in np.arange(0, T+h, h): #１周期分の計算
        if ik<=D:
            ik1 =SWon(E, E0, L, ik, t)



        else:
            if t <= ton:
                ik1 =SWon(E, E0, L, ik, t)
                sys = 1
            else:
                toff = t - ton
                ik1 = SWoff(E0, L, ir, toff)
                sys = 0
        if count >= write:
            time +=h
            #print("%f %f" %(time, ik1))
            if sys == 1:
                if count == write:
                    i_list = np.array([time, ik1])
                    #i_list = np.array([[time, ik1]])
                else:
                    #i_list = np.append(i_list, [[time, ik1]], axis=0)
                    i_list = np.vstack((i_list, [time, ik1]))  #txtファイルなどに書き込む場合は print("%f %f" %(time, clk), file=fp3)
            else:
                if count == write:
                    #i_list = np.array([[time, ik1]])
                    i_list = np.array([time, ik1])
                else:
                    #i_list = np.append(i_list, [[time, ik1]], axis=0)
                    i_list = np.vstack((i_list, [time, ik1]))

    ik = ik1
    sys = 1

    if count >= write:
        for clk in np.arange(0, 3+1e-13, 5e-3):
            if count == write:
                clk_list=np.array([[time, clk]])
                ir_list=np.array([[time, ir]])
            else:
                clk_list=np.append(clk_list, [[time, clk]], axis=0)
                ir_list=np.append(ir_list, [[time, ir]], axis=0)


#2次元配列の列の取り出しは、np.ndarray型だとnplist[x, :]でいけるけど、
# listはfor文とか使って書かないといけないから、list=np.arrayでndarray型に変えてやるといいと思う
# もしくは、最初にi_up_list = []ではなくi_up_list = np.array([])にする
#plt=散布図形式、plot=点をつなぐ
plt.scatter(i_list[:, 0], i_list[:, 1], s=1, c="r") 
plt.scatter(clk_list[:, 0], clk_list[:, 1], s=1, c="g") #list
plt.plot(ir_list[:, 0], ir_list[:, 1], c="orange")
plt.show()