#!/usr/bin/python 
# -*- coding: latin-1 -*-

# Codice iniziale degli studenti: Corso Quilici ed Elia Romani
# corso di Laboratorio per le applicazioni, matematica, universita' di Firenze
# docente: Emanuele Paolini

import pygame
import random
import sys
import itertools

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __rmul__(b, a):
        return Vector(a*b.x, a*b.y)

    def __sub__(a, b):
        return Vector(a.x - b.x, a.y - b.y)

    def __add__(a, b):
        return Vector(a.x + b.x, a.y + b.y)

    def int_tuple(self):
        return (int(self.x), int(self.y))
    
def dot(v, w):
    return v.x * w.x + v.y * w.y

def sqr(v):
    return v.x**2 + v.y**2


class Ball(object):
    def __init__(self, position, color, radius):
        self.speed = Vector(random.randint(-5,5), random.randint(-5,5))
        self.position = position
        self.radius = int(radius)
        self.mass = radius**2
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, ball.position.int_tuple(), ball.radius, 0)

    def check_bounce(self, other):
        if sqr(self.position - other.position) < (self.radius + other.radius)**2:
            dx = self.position - other.position
            dv = self.speed - other.speed
            try:
                c = 2.0 / (self.mass + other.mass) * dot(dv, dx) / sqr(dx)
            except ZeroDivisionError:
                c = 1.0
            self.speed -= other.mass * c * dx
            other.speed += self.mass * c * dx


class Box(object):
    def __init__(self, dimensions):
        self.dimensions = dimensions

    def random_position(self, radius=40):
        return Vector(random.randint(int(radius), self.dimensions.x - radius),
                      random.randint(int(radius), self.dimensions.y - radius))

    def check_bounce(self, ball):
        if ball.position.x - ball.radius < 0 and ball.speed.x < 0:
            ball.speed.x *= -1
        if ball.position.x + ball.radius > self.dimensions.x and ball.speed.x > 0:
            ball.speed.x *= -1
        if ball.position.y - ball.radius < 0 and ball.speed.y < 0:
            ball.speed.y *= -1
        if ball.position.y + ball.radius > self.dimensions.y and ball.speed.y > 0:
            ball.speed.y *= -1
        
    
if __name__ =='__main__':
    box = Box(Vector(1000, 700))

    pygame.init()
    window = pygame.display.set_mode(box.dimensions.int_tuple())
    pygame.display.set_caption("bouncing balls")
    clock = pygame.time.Clock()
    
    num_balls = 50
    ball_list = []
    while len(ball_list) < num_balls:
        ball_list.append(Ball(position=box.random_position(),
                              color=tuple(random.randint(0,255) for _ in range(3)),
                              radius=random.randint(16, 400)**0.5))
        
    while True:  # MAIN LOOP
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                sys.exit(0)

        window.fill ((255, 255, 255))  # white background
    
        # rimbalzo fra di loro
        for ball1, ball2 in itertools.combinations(ball_list, 2):
            ball1.check_bounce(ball2)
                         
        # rimbalzo sui muri                       
        for ball in ball_list:
            box.check_bounce(ball)

        # movimento
        for ball in ball_list:
            ball.position += ball.speed
            ball.draw(window)

        clock.tick(60)
        pygame.display.update()
