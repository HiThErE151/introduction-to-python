"""
zones.the_void.rooms
────────────────────
Room definitions for The Void zone.  Vnum range: 1 – 99.

Each room entry calls O.spawn() / M.spawn() to place fresh object and mob
instances.  Calling spawn() twice places two independent copies, so loot
or damage on one never affects the other.

Exit roomIds must match vnums defined here or in another loaded zone.
"""

from ashenmoor.world import Room
from . import objects as O
from . import mobs as M

ROOMS: dict[int, Room] = {
    1: Room(
        {
            "number": 1,
            "name": "&yT&bh&re &yI&bn&rn&N",
            "description": "The local inn of your childhood town",
            "indoors": True,
            "terrain": "wooden",
            "exits": [
                {"direction": "up", "roomId": 99004, "external": True},
            ],
            "objects": [
                O.spawn("wallet"),
            ],
            "mobs": [M.spawn("The_Inn_Maid")],  # two independent students
        }
    ),
    2: Room(
        {
            "number": 2,
            "name": "Downtown &yT&bo&rk&yy&bo",
            "description": "The bussling capitol of Japan, full of weebs and cars",
            "indoors": False,
            "terrain": "city",
            "exits": [
                {"direction": "east", "roomId": 99004, "external": True},
            ],
            "mobs": [M.spawn("Bob"), M.spawn("Hatsune_Miku")],
        }
    ),
}
