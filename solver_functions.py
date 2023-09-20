import numpy as np


def delta_t(cfl,dz,a):
    dt = cfl * dz / a
    return dt

def finite_diferences(v,i):
    y = v[i+1] - v[i]
    return y


def solver(dt, dz, u, par1, par2,par3):
    m = np.shape(u)[0]
    n = np.shape(u)[1]


    return 2
