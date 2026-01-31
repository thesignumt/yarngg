import pygame as pg
from dataclasses import dataclass, field
from typing import Tuple, Callable, Optional

pg.font.init()


# +--------------------------------------------------------+
# [                          text                          ]
# +--------------------------------------------------------+
def render_text(
    text: str,
    font_size: int = 24,
    color: Tuple[int, int, int] = (0, 0, 0),
    font_name: Optional[str] = None,
) -> pg.Surface:
    """Render text to a Surface."""
    font = pg.font.SysFont(font_name, font_size)
    return font.render(text, True, color)


# +--------------------------------------------------------+
# [                         button                         ]
# +--------------------------------------------------------+
@dataclass
class Button:
    rect: pg.Rect
    color: Tuple[int, int, int] = (200, 200, 200)
    text: str = ""
    text_color: Tuple[int, int, int] = (0, 0, 0)
    font_size: int = 24
    callback: Optional[Callable] = None
    surface: pg.Surface = field(init=False)

    def __post_init__(self):
        self.surface = (
            render_text(self.text, self.font_size, self.text_color)
            if self.text
            else None
        )

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)
        if self.surface:
            text_rect = self.surface.get_rect(center=self.rect.center)
            screen.blit(self.surface, text_rect)

    def handle_event(self, event: pg.event.Event):
        if self.callback and event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


# +--------------------------------------------------------+
# [                      box / panel                       ]
# +--------------------------------------------------------+
@dataclass
class Panel:
    rect: pg.Rect
    color: Tuple[int, int, int] = (100, 100, 100)
    border_color: Optional[Tuple[int, int, int]] = None
    border_width: int = 2

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, self.rect)
        if self.border_color:
            pg.draw.rect(screen, self.border_color, self.rect, self.border_width)
