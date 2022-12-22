import tcod
import entity_factory
import copy

from proceduralgeneration import generate_dungeon
from engine import Engine


def main():
    WIDTH = 80
    HEIGHT = 50

    MAP_WIDTH = 160
    MAP_HEIGHT = 100
    TILESET = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8,
        tcod.tileset.CHARMAP_TCOD
    )
    TITLE = "ROGUELIKE DEV"

    MAP_WIDTH = WIDTH
    MAP_HEIGHT = HEIGHT - 5

    ROOM_MAX_SIZE = 10
    ROOM_MIN_SIZE = 6
    MAX_ROOMS = 20
    MAX_MONSTERS_PER_ROOM = 3

    engine = Engine(player=player)
    
    # PLAYER ENTITY
    player = copy.deepcopy(entity_factory.player)

    engine.game_map = generate_dungeon(
        engine=engine,
        max_rooms=MAX_ROOMS,
        room_min_size=ROOM_MIN_SIZE,
        room_max_size=ROOM_MAX_SIZE,
        map_width=MAP_WIDTH,
        map_height=MAP_HEIGHT,
        max_monsters_per_room=MAX_MONSTERS_PER_ROOM
        )

    engine.update_fov()
    

    with tcod.context.new_terminal(
        WIDTH, HEIGHT,
        tileset=TILESET,
        title=TITLE, vsync=True
    ) as context:
        root_console = tcod.Console(WIDTH, HEIGHT, order="F")

        #main game loop
        while True:
            engine.render(console=root_console, context=context, player=player) # RENDERS MAP
            engine.event_handler.handle_events()


if __name__ == "__main__": main()