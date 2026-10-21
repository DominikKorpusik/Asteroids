import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    

    while True:
        log_state()
        dt = clock.tick(60) / 1000
        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)

        updatable.update(dt)


        for ast in asteroids:
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    ast.split()
                    shot.kill()

        for ast in  asteroids:
            if player.collides_with(ast):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

if __name__ == "__main__":
    main()
