from game_map import GameMap

from typing import TYPE_CHECKING

import random
import tcod
import tiles
import entity_factory

if TYPE_CHECKING:
    from engine import Engine

class RectangularRoom:
    def __init__(self, x, y, width, height):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self):
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self):
        """Return the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

    def intersects(self, other_room):
        return(
            self.x1 <= other_room.x2
            and self.x2 >= other_room.x1
            and self.y1 <= other_room.y2
            and self.y2 >= other_room.y1
        )


def place_entities(room, dungeon, max_monsters):
    num_of_monsters = random.randint(0, max_monsters)

    for i in range(num_of_monsters):
        x = random.randint(room.x1 + 1, room.x2 - 1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        # check if there is already entity there
        if not any(entity.x == x and entity.y == y for entity in dungeon.entities):
            if random.random() < 0.6:
                entity_factory.slime.spawn(dungeon, x, y)
            else:
                entity_factory.angry_mushroom.spawn(dungeon, x, y)


def tunnel_between(start, end):
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:
        corner_x, corner_y = x2, y1
    else:
        corner_x, corner_y = x1, y2
    
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y


def generate_dungeon(
    max_rooms,
    room_min_size, room_max_size,
    map_width, map_height,
    engine,
    max_monsters_per_room
):
    player = engine.player
    dungeon = GameMap(engine, map_width, map_height, entities=[player])

    rooms = []

    for r in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        new_room = RectangularRoom(x, y, room_width, room_height)

        if any(new_room.intersects(other_room) for other_room in rooms):
            continue


        if len(rooms) == 0:
            player.place(*new_room.center, dungeon)            
        else:
            for x, y, in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tiles.tunnel

        #dungeon.tiles[new_room.inner] = tiles.floor
        place_entities(new_room, dungeon, max_monsters_per_room)

        rooms.append(new_room)
    
    for r in rooms:
        dungeon.tiles[r.inner] = tiles.floor

    return dungeon