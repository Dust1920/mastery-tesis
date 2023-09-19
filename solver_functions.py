import numpy as np
import model_functions as model

"""
Aqui presentaremos el código para el método upwind.


def upwind(dt, dz, u, vpar2, w):
    m = np.shape(u)[0]
    aux = np.zeros((m, 5))
    dzt = dt / dz
    vt0 = vpar2[0]
    vtnd = vpar2[1]
    q_star = vpar2[2]
    vel = u[:, 0]
    tem = u[:, 1]
    qv = u[:, 2]
    qr = u[:, 3]
    qn = u[:, 4]

    cflvt = np.zeros(m)
    cflvn = np.zeros(m)

    for i in range(1, m - 1):
        cflvt[i] = w - get_terminalvelocity(vt0, qr[i], q_star)
        cflvn[i] = w - get_aerosolvelocity(vtnd, vt0, qr[i], q_star)

        if w < 0:
            aux[i, 0] = w
            aux[i, 1] = tem[i] - dzt * w * (tem[i + 1] - tem[i])
            aux[i, 2] = qv[i] - dzt * w * (qv[i + 1] - qv[i])
        else:
            aux[i, 0] = w
            aux[i, 1] = tem[i] - dzt * w * (tem[i] - tem[i - 1])
            aux[i, 2] = qv[i] - dzt * w * (qv[i] - qv[i - 1])
        if cflvt[i] < 0:
            aux[i, 3] = qr[i] - dzt * ((w - get_terminalvelocity(vt0, qr[i + 1], q_star)) * qr[i + 1]
                                       - (cflvt[i] * qr[i]))
        else:
            aux[i, 3] = qr[i] - dzt * ((w - get_terminalvelocity(vt0, qr[i], q_star)) * qr[i] -
                                       (w - get_terminalvelocity(vt0, qr[i - 1], q_star)) * qr[i - 1])
        if cflvn[i] < 0:
            aux[i, 4] = (qn[i] - dzt *
                         ((w - get_aerosolvelocity(vtnd, vt0, qr[i + 1], q_star)) * qn[i + 1] - (
                                 w - get_aerosolvelocity(vtnd, vt0, qr[i], q_star)) * qn[i]))
        else:
            aux[i, 4] = (qn[i] - dzt *
                         ((w - get_aerosolvelocity(vtnd, vt0, qr[i], q_star)) * qn[i] - (
                                 w - get_aerosolvelocity(vtnd, vt0, qr[i - 1], q_star)) * qn[i - 1]))
        aux[0, :] = aux[1, :]  # Antes de cambiarlo, funciona.
        aux[-1, :] = aux[-2, :]
        # print(get_terminalvelocity(vt0, aux[i, 3], q_star))
    pt = np.max(np.abs(cflvt))
    pn = np.max(np.abs(cflvn))
    p0 = np.max(np.abs(aux[:, 0]))
    p = np.max([pn, pt, p0])
    return aux, p


def resol_test(t_0, t_f, cfl, dt, dz, workspace, q_parameters, v0, tick):
    tick_time = 0
    while t_0 < t_f:
        q = upwind(dt, dz, workspace, q_parameters, v0)
        workspace = q[0]
        dt = cfl * dz / np.abs(q[1])
        print("cfl = ", dt / dz * q[1])
        tick_time += 1
        if tick_time == tick:
            # print(workspace)
            break
        t_0 += dt
        # print(q[1])
    return workspace
"""
