from __future__ import annotations

import copy
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    gamemap: GameMap

    def __init__(
        self, gamemap=None, char="?",
        fg_colour=(255, 255, 255), bg_colour=(255,255,255),
        name="<Unnamed>", blocks_movement=False
    ): 
        # colour is represented as a tuple RGB value
        self.char = char
        self.fg_colour = fg_colour
        self.bg_colour = bg_colour
        self.name = name
        self.blocks_movement = blocks_movement
        if gamemap:
            self.gamemap = gamemap
            gamemap.entities.add(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def spawn(self, gamemap, x, y):
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        clone.gamemap = gamemap
        gamemap.entities.add(clone)

        return clone

    def place(self, x, y, gamemap):
        self.x = x
        self.y = y
        if gamemap:
            if hasattr(self, "game_map"): # possibly unitialized
                self.gamemap.entities.remove(self)
            self.gamemap = gamemap
            gamemap.entities.add(self)