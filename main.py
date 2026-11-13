import src.sim
import pygame
import numpy as np

scale = src.sim.scale
player = src.sim.player
sensor = src.sim.sensor
player_sensor = src.sim.player_sensor

dt = 1/10;
for i in range (3150):


    src.sim.run()

    # reality
    dx = scale * dt * np.cos(player.angle) * player.vel
    dy = scale * dt * np.sin(player.angle) * player.vel
    player.position_x += dx
    player.position_y += dy
    player.angle += dt*player.ang_vel

    # sensor update
    sensor.velocity(player.vel)
    sensor.ang_velocity(player.ang_vel)

    # player sensor 

    dx = scale * dt * np.cos(player_sensor.angle) * sensor.vel
    dy = scale * dt * np.sin(player_sensor.angle) * sensor.vel
    player_sensor.position_x += dx
    player_sensor.position_y += dy
    player_sensor.angle += dt * sensor.ang_vel

    # Standard EKF-SLAM

    # Right-invariant EKF (R-IEKF)

    # Loop refresh

    sensor.detections = []
    src.sim.clock.tick(10) # Euler discretization, ∆t = 0.1 s
