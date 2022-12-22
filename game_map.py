import numpy as np
from tcod.console import Console

from typing import TYPE_CHECKING

import tiles

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity


class GameMap:
    def __init__(self, engine, width, height, entities):
        self.engine = engine
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tiles.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")
        self.explored = np.full((width, height), fill_value=False, order="F")

        self.entities = set(entities)

    
    def get_blocking_entity_at_location(self, location_x, location_y,):
        for entity in self.entities:
            if entity.blocks_movement and entity.x == location_x and entity.y == location_y:
                return entity

        return None


    def in_bounds(self, x, y):
        # check if position is in bounds on map
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console, player):
        console.tiles_rgb[
            0:self.width,
            0:self.height
        ] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tiles.SHROUD,
        )

        for entity in self.entities:
            if self.visible[entity.x, entity.y]:
                console.print(x=entity.x, y=entity.y, string=entity.char,
                fg=entity.fg_colour, bg=entity.bg_colour)

    def update_map_fov(self):
        self.tiles
