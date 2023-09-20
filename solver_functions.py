def finite_diferences(v,i,side):
    if side == 1:
        m = v[i + 1] - v[i]
    else:
        m = v[i] - v[i - 1]
    return m

def solver(dt, dz, u, par1, par2):
    return 2


def wvt(w,qr):
    return w - vt(qr)

def wvn(w,qr,par):
    return w - vtn(par, qr)