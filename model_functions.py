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
    b = theta_0 + tem_rate * z
    return b


def bouyancy_force(par, theta, qv, qr, z):
    #  bvp = np.array([temperature_ref, temperature_rate, g, epsilon, qv0, lcp, desaceleration])
    theta_0 = par[0]
    g = par[2]
    eps = par[3]
    qv0 = par[4]
    theta_env = theta_hat(z,par)
    qv_hat = approxfqv(z, qv0)
    f = g / theta_0 * (theta - theta_env + eps * theta_0 * (qv - qv_hat) - theta_0 * qr)
    return f


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
    return y

def w_vt(w,qr,par):
    y = w - vt(qr, par)
    return y


def w_vtn(w, qr, par):
    y = w - vtn(qr, par)
    return y


# Condensation and Evaporation functions
def tau_c(q_n,par,qn_0):
    tau_0 = par[0]
    gamma = par[1]
    tau_c = tau_0 * np.exp(-((q_n - qn_0)/ gamma) ** 2)
    return tau_c


def condensation(qv,qn,z,qn_0, par):
    qvs0 = par[2]
    dif = qv - approxfqv(z, qvs0)
    cd = tau_c(qn, par, qn_0) ** (-1) * np.max([dif, 0])
    return cd 


def evaporation(qv,qr,z,par):
    qvs0 = par[2]
    tau_e = par[3]
    q_star = par[4]
    dif = approxfqv(z,qvs0) - qv
    ev = qr * (tau_e * q_star)**(-1) * np.max([dif, 0])
    return ev

def co_ev(qv,qr,qn,z,qn_0,par):
    y = condensation(qv,qn,z,qn_0,par) - evaporation(qv,qr,z,par)
    return y