import intro
import solver_functions as sol
import numpy as np
import plot_functions as vf

"""
Resolución del modelo Determinista FARE.
"""

dz = intro.h_region[1] - intro.h_region[0]
cfl = 0.5
a0 = 1
delta_t = sol.delta_t(cfl,dz,a0)

# Zona de trabajo
n_var = len(intro.variables)
n_z = intro.n_h

workspace = np.zeros((n_z,n_var))

