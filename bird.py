from pico2d import *
import random

import game_framework

# bird run speed
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 25.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# bird Action Speed
# fill here
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Bird:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x, self.y = random.randint(100, 1500), random.randint(300, 500)
        self.w, self.h = 50, 50  # 1.5m, 1.5m
        self.dir = 1
        self.frame = 0
        self.action = 2

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time

        if self.x > 1500 or self.x < 100:
            self.dir *= -1


    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame) * 183, self.action * 168, 183, 168, self.x, self.y, self.w, self.h)
        else:
            self.image.clip_composite_draw(int(self.frame) * 183, self.action * 168, 183, 168, 0, 'h',  self.x, self.y, self.w, self.h)


