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

def cfl_criter(omega,wqn,wqr):
    y = np.concatenate((omega,wqn,wqr))
    ytop = np.max(np.abs(y))
    return ytop


def upwind(dt, dz, u, bou_param, q_param, cdev_param, height):
    m = np.shape(u)[0]
    n = np.shape(u)[1]
    omega = u[:, 0]
    theta = u[:, 1]
    qv = u[:, 2]
    qr = u[:, 3]
    qn = u[:, 4]
    dzt = dt / dz
    tau_w = bou_param[-1]  # bou_param: Bouyancy_force
    aux = np.zeros((m,n))
    fqr = f_qr(omega,height,q_param) # q_param: qr,qn parameters
    fqn = f_qn(omega,height,qr,q_param)
    for i in np.arange(1, m - 1):
        aux[i, 0] = omega[i] + dt * (mf.bouyancy_force(bou_param,theta[i],qv[i],qr[i],height[i]) - omega[i] / tau_w)
        # aux[i, 0] = 1
        if omega[i] < 0:
            aux[i, 1] = theta[i] - dzt * omega[i] * finite_diferences(theta, i)
            aux[i, 2] = qv[i] - dzt * omega[i] * finite_diferences(qv, i)
        else:
            aux[i, 1] = theta[i] - dzt * omega[i] * finite_diferences(theta, i - 1)
            aux[i, 2] = qv[i] - dzt * omega[i] * finite_diferences(qv, i - 1)
        if mf.w_vt(omega[i],qr[i],q_param) < 0:
            aux[i, 3] = qr[i] - dzt * finite_diferences(fqr, i)
        else:
            aux[i, 3] = qr[i] - dzt * finite_diferences(fqr, i - 1)
        if mf.w_vtn(omega[i],qr[i],q_param) < 0:
            aux[i, 4] = qn[i] - dzt * finite_diferences(fqn, i)
        else:
            aux[i, 4] = qn[i] - dzt * finite_diferences(fqn, i - 1)
    aux[-1, : ] = aux[-2, :]
    aux[0, :] = aux[1, : ]
    return aux,fqn,fqr

def solver(dt, dz, u, bou_param, q_param, cdev_param, height, tf, cfl):
    t0 = 0
    while t0 < tf:
        u, fr, fn = upwind(dt, dz, u, bou_param, q_param, cdev_param, height)
        dt = cfl * dz / cfl_criter(u[:,1],fr,fn)
        t0 = t0 + dt
        print(t0)
    return u
