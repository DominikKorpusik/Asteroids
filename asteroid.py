import random

from pygame import Surface
import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_KINDS, ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS, ASTEROID_SPAWN_RATE_SECONDS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        else:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)
            first_asteroid_velocity = self.velocity.rotate(rand)
            second_asteroid_velocity = self.velocity.rotate(-rand)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = first_asteroid_velocity * 1.2
            second_asteroid.velocity = second_asteroid_velocity * 1.2
