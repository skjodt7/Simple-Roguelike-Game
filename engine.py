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
    gamemap: GameMap

    def __init__(self, player):
        self.event_handler: EventHandler = EventHandler(self)
        self.player = player

    def update_fov(self):
        self.gamemap.visible[:] = compute_fov(
            self.gamemap.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=100
        )
        self.gamemap.explored |= self.gamemap.visible

    def render(self, console, context, player):
        self.gamemap.render(console, player) # render tiles

        context.present(console)
        console.clear()

    def handle_enemy_turns(self):
        for entity in self.gamemap.entities:
            print(f"The {entity.name} wonders about aimlessly.")

        