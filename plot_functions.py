import matplotlib.pyplot as plt
import scale
"""
Aqui estarán las funciones auxiliares para la visualización del comportamiento del modelo. 
"""

def visual_system(u, space):
    w = u[:, 0]
    t = u[:, 1]
    qv = u[:, 2]
    qr = u[:, 3]
    qn = u[:, 4]
    fig_wt, wt = plt.subplots(1,2, sharey= True)
    fig_wq, wq = plt.subplots(2,2, sharey= True)

    wt[0].plot(w * scale.velocity, space * scale.height)
    wt[1].plot(t * scale.temperature, space * scale.height)

    wq[0,0].plot(w * scale.velocity, space * scale.height)
    wq[0,1].plot(qv * scale.ratio, space * scale.height)
    wq[1,0].plot(qr * scale.ratio, space * scale.height)
    wq[1,1].plot(qn * scale.ratio, space * scale.height)
    plt.show()