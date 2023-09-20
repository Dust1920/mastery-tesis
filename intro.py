import scale
import numpy as np

 
variables = ['v','theta','qv','qr','qn']  # PDSEs Variables
z_final = 15   # final height (tropopause) (assume h_initial = 0).
n_h = 64       # grid points on height.
t_final = 1    # final tiem (assume t_initial = 0).

# Adimensionalization
z_final = z_final / scale.height
t = t_final / scale.time

# Discretization
h_region = np.linspace(0,z_final,n_h)

# To System Model
initial = [variables, z_final, t_final,h_region]
