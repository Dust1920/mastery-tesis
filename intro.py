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

# Initial functions
a_omega = 8
a_temp = 8
a_qv = 8
a_qr = 8
a_qn = 8

a_omega = a_omega / scale.height
a_temp = a_temp / scale.height
a_qv = a_qv / scale.height
a_qr = a_qr / scale.height
a_qn = a_qn / scale.height

# Heaviside function
def heaviside(z,a):
    if z < a:
        y = 0
    else:
        y = 1
    return y



def initial_velocity(z_vector):
    y = [heaviside(i,a_omega) for i in z_vector]
    return y
    
    
def initial_temperature(z_vector):
    y = [heaviside(i,a_temp) for i in z_vector]
    return y
    
def initial_qv(z_vector):
    y = [heaviside(i,a_qv) for i in z_vector]
    return y
    
def initial_qr(z_vector):
    y = [heaviside(i,a_qr) for i in z_vector]
    return y
    
def initial_qn(z_vector):
    y = [heaviside(i,a_qn) for i in z_vector]
    return y