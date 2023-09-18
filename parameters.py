import scale
import numpy as np


# B
temperature_rate = 3  # K / km
temperature_rate = temperature_rate * scale.height / scale.temperature

# L, C_p
latent_heat = 2.5e6  # Calor latente
latent_heat = scale.mass / scale.energy * latent_heat
specific_heat = 1e3  # Calor específico a presión constante.
specific_heat = (specific_heat / scale.energy) * (scale.mass * scale.temperature)

lcp = latent_heat / specific_heat

# epsilon
epsilon = 0.6

# tau_w
tau_w = 7.5  # min
tau_w = tau_w / scale.time

# gravity
g = 9.81  # m/s^2
g = (g / scale.velocity) * 60 * scale.time


q_star = 10
q_star = q_star / scale.ratio


b_w = 0.491  # m/s sqrt(s)
b_w = (b_w / scale.velocity) * scale.time * 60 * np.sqrt(60 * scale.time)

tau0 = 0.1
gamma = 0.3
taue = 0.2
c = 0.2
c0 = 0.4


vt0 = 1
vtnd = 1

