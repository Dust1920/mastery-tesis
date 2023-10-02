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

workspace[:, 0] = intro.initial_velocity(intro.h_region)
workspace[:, 1] = intro.initial_temperature(intro.h_region)
workspace[:, 2] = intro.initial_qv(intro.h_region)
workspace[:, 3] = intro.initial_qr(intro.h_region)
workspace[:, 4] = intro.initial_qn(intro.h_region)

vf.visual_system(workspace, intro.h_region)


