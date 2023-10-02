import numpy as np
import model_functions as mf

def delta_t(cfl,dz,a):
    dt = cfl * dz / a
    return dt


def finite_diferences(v,i):
    y = v[i+1] - v[i]
    return y


def f_qr(omega,height,par):
    o = len(height)
    y = [mf.w_vt(omega[i],height[i],par) for i in range(o)]
    return y


def f_qn(omega, height, qr, par):
    o = len(height)
    y = [mf.w_vtn(omega[i], qr[i], par) for i in range(o)]
    return y


def solver(dt, dz, u, par1, par2, par3, height):
    m = np.shape(u)[0]
    n = np.shape(u)[1]
    omega = u[:, 0]
    theta = u[:, 1]
    qv = u[:, 2]
    qr = u[:, 3]
    qn = u[:, 4]
    dzt = dt / dz
    tau_w = par1[-1]  # par1: Bouyancy_force
    aux = np.zeros((m,n))
    aux = u
    fqr = f_qr(omega,height,par2) # par2: qr,qn parameters
    fqn = f_qn(omega,height,qr,par2)
    for i in np.arange(1, m - 1):
        aux[i, 0] = omega[i] + dt
        if omega[i] > 0:
            aux[i, 1] = theta[i] - dzt * omega[i] * finite_diferences(theta, i)
            aux[i, 2] = qv[i] - dzt * omega[i] * finite_diferences(qv, i)
        else:
            aux[i, 1] = theta[i] - dzt * omega[i] * finite_diferences(theta, i - 1)
            aux[i, 2] = qv[i] - dzt * omega[i] * finite_diferences(qv, i - 1)
        if mf.w_vt(omega[i],qr[i],par2) > 0:
            aux[i, 3] = qr[i] - dzt * finite_diferences(fqr, i)
        else:
            aux[i, 3] = qr[i] - dzt * finite_diferences(fqr, i - 1)
        if mf.w_vtn(omega[i],qr[i],par2) > 0:
            aux[i, 4] = qn[i] - dzt * finite_diferences(fqn, i)
        else:
            aux[i, 4] = qn[i] - dzt * finite_diferences(fqn, i - 1)
    return aux
