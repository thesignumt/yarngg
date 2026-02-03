import pygame
from dataclasses import dataclass, field
from typing import Callable

pygame.font.init()


# +--------------------------------------------------------+
# [                          text                          ]
# +--------------------------------------------------------+
def render_text(
    text: str,
    font_size: int = 24,
    color: tuple[int, int, int] = (0, 0, 0),
    font_name: str | None = None,
) -> pygame.Surface:
    """Render text to a Surface."""
    font = pygame.font.SysFont(font_name, font_size)
    return font.render(text, True, color)


# +--------------------------------------------------------+
# [                         button                         ]
# +--------------------------------------------------------+
@dataclass
class Button:
    rect: pygame.Rect
    color: tuple[int, int, int] = (200, 200, 200)
    text: str = ""
    text_color: tuple[int, int, int] = (0, 0, 0)
    font_size: int = 24
    callback: Callable | None = None
    surface: pygame.Surface | None = field(init=False)

    def __post_init__(self):
        self.surface = (
            render_text(self.text, self.font_size, self.text_color)
            if self.text
            else None
        )

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.surface:
            text_rect = self.surface.get_rect(center=self.rect.center)
            screen.blit(self.surface, text_rect)

    def handle_event(self, event: pygame.event.Event):
        if self.callback and event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


# +--------------------------------------------------------+
# [                      box / panel                       ]
# +--------------------------------------------------------+
@dataclass
class Panel:
    rect: pygame.Rect
    color: tuple[int, int, int] = (100, 100, 100)
    border_color: tuple[int, int, int] | None = None
    border_width: int = 2

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.border_color:
            pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
