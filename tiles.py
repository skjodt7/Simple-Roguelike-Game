"""
The map itself will be made up of tiles, which will contain certain data about
if the tile is “walkable” (True if it’s a floor, False if its a wall), 
“transparency” (again, True for floors, False for walls), 
and how to render the tile to the screen.
"""

import numpy as np

# tile graphics compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),
        ("fg", "3B"), # 3 unsigned bytes, for rgb values
        ("bg", "3B"),
    ]
)

# tile structure used for tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool),
        ("transparent", np.bool),
        ("dark", graphic_dt),
        ("light", graphic_dt),
    ]
)

def new_tile(walkable, transparent, dark, light):
    # used to define individual tile types
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD: unseen and unexplored tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True, transparent=True,
    dark=(ord(" "), (255, 255, 255), (101, 38, 140)),
    light=(ord(" "), (255, 255, 255), (151, 88, 190))
    )

wall = new_tile(
    walkable=False, transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 7, 69)),
    light=(ord(" "), (255, 255, 255), (46, 57, 119))
    )

tunnel = new_tile(
    walkable=True, transparent=True,
    dark=(ord(" "), (237, 164, 194), (101, 38, 140)),
    light=(ord(" "), (237, 164, 194), (151, 88, 190))
)