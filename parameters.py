import scale
import numpy as np


# Bouyancy and friction parameters
temperature_ref = 300  # K
temperature_rate = 3   # K / km
latent_heat = 2.5e6    # Calor latente
specific_heat = 1e3    # Calor específico a presión constante.
epsilon = 0.6
g = 9.81               # m/s^2
qv_0 = 16
qvs_0 = 28

g = (g / scale.velocity) * (60 * scale.time)
temperature_ref = temperature_ref / scale.temperature
temperature_rate = temperature_rate * scale.height / scale.temperature
latent_heat = scale.mass / scale.energy * latent_heat
specific_heat = (specific_heat / scale.energy) * (scale.mass * scale.temperature)
qv_0 = qv_0 / scale.ratio
qvs_0 = qvs_0 / scale.ratio

lcp = latent_heat / specific_heat

desaceleration = 7.5  # min
desaceleration = desaceleration / scale.time

bfp = np.array([temperature_ref, temperature_rate, g, epsilon, qv_0, lcp, desaceleration])


# aerosol and terminal velocity parameters
vt0 = 1
q_star = 10
vtnd = 1

vt0 = vt0 / scale.velocity
q_star = q_star / scale.ratio
vtnd = vtnd / scale.velocity
atvp = np.array([vt0, q_star, vtnd])


# condensation and evaporation parameters
tau_0 = 0.1
tau_c = 2
gamma = 0.3
tau_e = 0.2
c = 0.2
c_0 = 0.4

cep = np.array([tau_0, gamma, qvs_0, tau_e, q_star])


# stochastic parameters
b_w = 0.491  # m/s sqrt(s)
b_w = (b_w / scale.velocity) * scale.time * 60 * np.sqrt(60 * scale.time)
