import numpy as np
import src.map

sigma_z = 0.5
sigma_v = 0.2
sigma_w = 10 * np.pi / 180 # radians per second

scale_pos = 30

def perturb(sigma, scale = 1):
    return scale * np.random.normal(0, sigma)

class Sensor():
    def __init__(self):
        self.detections = []
        self.vel = 1;
        self.ang_vel = 0.1

    def update(self, identity, pos):
        self.detections.append([identity, [pos[0] + perturb(sigma_z, scale_pos)]])

    def velocity(self, vel = 1):
        self.vel = vel + perturb(sigma_v)

    def ang_velocity(self, ang_vel = 0.1):
        self.ang_vel = ang_vel + perturb(sigma_w)
