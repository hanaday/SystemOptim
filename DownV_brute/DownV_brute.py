import numpy as np
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
    maxmap = 10
    E0 = 13.7
    L = 1.e-3
    ir = 2.5
    ik = 0
    eps = 1e-6
    f_start, f_end, f_step = 10e3, 100e3, 1e3 # [Hz]
    E_start, E_end, E_step = 20, 50, 0.1 # [V]

    f_roof = int((f_end - f_start)/f_step)
    E_roof = int((E_end - E_start)/E_step)
    img = np.zeros((f_roof+1, E_roof+1, 3))

    for id_f, f in enumerate(range(int(f_start/f_step), int(f_end/f_step)+1, 1)):
        f = f * f_step
        T = 1/f
        for id_E, E in enumerate(range(int(E_start/E_step), int(E_end/E_step)+1, 1)):
            E = E * E_step
            D = border(E, E0, L, T, ir)

            for count in range(500):
                ton = t_on(E, E0, L, ir, ik)
                toff = T - ton

                if ik <= D:
                    ik1 = return1(E, E0, L, T, ik)
                else:
                    ik1 = return2(E, E0, L, toff, ir, ik)
                ik = ik1

            map_ik = ik
            period = 0

            for i in range(maxmap+1):
                ton = t_on(E, E0, L, ir, ik)
                toff = T - ton

                if ik <= D:
                    ik1 = return1(E, E0, L, T, ik)
                else:
                    ik1 = return2(E, E0, L, toff, ir, ik)
                ik = ik1

                period += 1
                delta = abs(map_ik - ik)
                if delta < eps:
                    if period == 1:
                        img[f_roof - id_f, id_E, 0] = 255 # red
                    elif period == 2:
                        img[f_roof - id_f, id_E, 1] = 255 # green
                    elif period == 3:
                        img[f_roof - id_f, id_E, 2] = 255 # blue
                    elif period == 4:
                        img[f_roof - id_f, id_E, :] = 255, 255, 0 # yellow
                    elif period == 5:
                        img[f_roof - id_f, id_E, :] = 255, 0, 255 # magenta
                    elif period == 6:
                        img[f_roof - id_f, id_E, :] = 0, 255, 255 # aqua
                    elif period == 7:
                        img[f_roof - id_f, id_E, :] = 128, 128, 0 # olive
                    elif period == 8:
                        img[f_roof - id_f, id_E, :] = 128, 0, 128 # purple
                    elif period == 9:
                        img[f_roof - id_f, id_E, :] = 0, 128, 128 # teal
                    elif period == 10:
                        img[f_roof - id_f, id_E, :] = 255, 165, 0 # orange
                    elif period >= 11 and period <= maxmap:
                        img[f_roof - id_f, id_E, :] = 128, 128, 128 # gray
                    break
                elif period > maxmap:
                    img[f_roof - id_f, id_E, :] = 255, 255, 255 # white
                    break

            if id_f == 0 and id_E == 0:
                fig, ax = plt.subplots(figsize=(9,9)) 
                ax.set_xlabel("E [V]")
                ax.set_ylabel("f [kHz]")
                """
                ax.set_xticks([0, int(E_roof/5), int(E_roof/5*2), int(E_roof/5*3), int(E_roof/5*4), E_roof])
                x_step = int((E_end-E_start)/5)
                ax.set_xticklabels([E_start, E_start+x_step, E_start+x_step*2, E_start+x_step*3, E_start+x_step*4, E_end])
                ax.set_yticks([f_roof, int((f_roof)/5*4), int((f_roof)/5*3), int((f_roof)/5*2), int((f_roof)/5), 0])
                y_step = int((f_end-f_start)/5/1000)
                k_f_st = int(f_start/1000)
                ax.set_yticklabels([k_f_st, k_f_st+y_step, k_f_st+y_step*2, k_f_st+y_step*3, k_f_st+y_step*4, int(f_end/1000)])
                """
                image = ax.imshow(img.astype(np.uint8))
            else:
                image.set_data(img.astype(np.uint8))
                plt.pause(0.005)
    plt.savefig(f"./SystemOptim/DownV_brute/E-f_graph.jpg")