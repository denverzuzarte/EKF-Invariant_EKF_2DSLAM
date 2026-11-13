import pygame
import pygame.gfxdraw
import math
import numpy as np
from src.sensor import Sensor
import src.sensor

pygame.init()
clock = pygame.time.Clock()

scale = src.sensor.scale_pos

sigma_z = 0.5

sensor = Sensor()

def create_screen(height = 1080, width = 1920):
    return pygame.display.set_mode((width, height))

class Player():
    def __init__(self, screen, pos = [500, 500], color = "yellow", size = 50): 
        self.position_x = pos[0]
        self.position_y = pos[1]
        self.vel = 1;
        self.angle = 0;
        self.ang_vel = 0.1;
        self.size = size
        self.color = color
    def render(self):
        self.sqr = [self.position_x - self.size/2, self.position_y - self.size/2, 
                     self.size, self.size]
        pygame.gfxdraw.box(screen, self.sqr, self.color)
    
    def scan(self, obs_list):
        for obs in obs_list:
            dist = math.sqrt((self.position_x - obs.position_x)**2 +
                             (self.position_y - obs.position_y)**2)
            if dist < 5 * scale : 
                sensor.update(obs.identity, 
                              np.array([obs.position_x, obs.position_y]))

class Obstacle():
    def __init__(self, screen, pos = [600, 600], color = "red",  size = 20):
        self.position_x = pos[0]
        self.position_y = pos[1]
        self.size = size
        self.color = color
        self.identity = 0;
    def render(self):
        pygame.draw.circle(screen, self.color, [self.position_x, self.position_y], self.size)


s_height = 1080;
s_width = 1920;
middle = [s_width/2, s_height/2]

screen = create_screen(s_height, s_width)
running = True
player = Player(screen, pos = [middle[0], middle[1] - 10 * scale], color = [255,255,255,255]) # default player
player_sensor = Player(screen, pos = [middle[0], middle[1] - 10 * scale], color = [0,255,255,90])
obs_list =[]
n = 20
for i in range (n): 
    ''' 20 landmarks placed evenly in angle around the circle centre (0, 10)
    alternately at radius 7 m and 13 m.'''
    len = 7 if i % 2 else 13
    x = middle[0] + len * scale * np.cos(np.pi * 2 * i / n)
    y = middle[1] + len * scale * np.sin(np.pi * 2 * i / n)
    new_obs = Obstacle(screen, pos = [x, y]);
    new_obs.identity = i;
    obs_list.append(new_obs)

def run():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    for obs in obs_list:
        obs.render()
    player.render()
    player_sensor.render()
    pygame.display.flip()
    player.scan(obs_list)

if __name__ == "__main__":
    while running: 
        run();
    pygame.quit()
