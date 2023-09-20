import numpy as np

# Bouyancy functions
def approxfqv(z, c):
    # Dr.Gerardo Hernandez Dueñas
    a = 18.04
    b = 3.27
    c0 = 0.1
    d = 3.48
    bl = 1 - b * np.log(1 + c0 * z)
    if bl > 0:
        pz = bl ** d
        fqv = (c / pz) * np.exp(- a * (1 / ((1 - b * np.log(1 + c0 * z)) * (1 + c0 * z)) - 1))
        return fqv
    else:
        return "ERROR"

def theta_hat(z,par):
    theta_0 = par[0]
    tem_rate = par[1]
    return theta_0 + tem_rate * z


def bouyancy_force(par, qv, qr, z):
    






# aerosol and terminal velocity functions 
def vt(qr,par):
    vt0 = par[0]
    q_star = par[1]
    y = vt0 * qr / q_star
    return y
    
def vtn(qr,par):
    q_star = par[1]
    vtnd = par[2]
    y = vtnd + np.max([qr / q_star, 1]) * np.max([vt(qr,par)-vtnd],0)

def w_vt(w,qr,par):
    y = w - vt(qr, par)
    return y

def w_vtn(w, qr, par):
    y = w - vtn(qr, par)
    return y

