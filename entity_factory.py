from entity import Entity

player = Entity(char="@", fg_colour=(255, 255, 255), bg_colour=(151, 88, 190),
name="Player", blocks_movement=True)


slime = Entity(char="s", fg_colour=(37, 142, 115), bg_colour=(235, 156, 188),
name="Slime", blocks_movement=True)

angry_mushroom = Entity(char="M", fg_colour=(210, 40, 111), bg_colour=(35, 213, 163),
name="Enraged Mushroom", blocks_movement=True)