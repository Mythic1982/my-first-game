import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while (True):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update in updatable_group:
            update.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit()

            for shot in shot_group:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        
        for draw in drawable_group:
            draw.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
