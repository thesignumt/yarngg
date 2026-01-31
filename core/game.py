import pygame
from . import cfg

from ..utils import pygame_utils as pu


class Game:
    def __init__(self):
        self.running = True

        pygame.init()
        info = pygame.display.Info()
        w, h = info.current_w, info.current_h
        self.screen = pygame.display.set_mode((w, h), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # game logic here
        pass

    def draw(self):
        self.screen.fill(cfg.BLACK)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(cfg.FPS)

        pygame.quit()
