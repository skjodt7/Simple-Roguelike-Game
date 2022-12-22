from __future__ import annotations

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity
from input_handler import EventHandler

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap


class Engine:
    game_map: GameMap

    def __init__(self, player):
        self.event_handler: EventHandler = EventHandler(self)
        self.player = player

    def update_fov(self):
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=100
        )
        self.game_map.explored |= self.game_map.visible

    def render(self, console, context, player):
        self.game_map.render(console, player) # render tiles

        context.present(console)
        console.clear()

    def handle_enemy_turns(self):
        for entity in self.game_map.entities:
            pass
        