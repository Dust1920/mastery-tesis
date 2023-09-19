import numpy as np

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