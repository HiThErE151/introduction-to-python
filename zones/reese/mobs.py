"""
zones.the_void.mobs
───────────────────
Mob templates for The Void zone.

Add an entry to TEMPLATES for every NPC type that can appear in this zone.
Call spawn(key) to get a fresh independent Mob instance — place as many
copies in rooms as you like, each is independent.
"""

from ashenmoor.world import Mob
from ashenmoor.world.zone import make_spawner

TEMPLATES: dict[str, dict] = {
    "wandering_student": {
        "name": "a wandering student",
        "key_words": ("student", "wandering"),
        "room_description": "&wA wandering student meanders about aimlessly.&N",
        "description": (
            "A student with a faraway look, clearly lost in thought.\n"
            "Or possibly just lost."
        ),
        "race": "Human",
        "class": "Student",
        "level": 1,
        "stats": [60, 65, 60, 80, 70, 75],
        "aggro": False,
        "wander": True,
    },
    "Lucas": {
        "name": "Lucas",
        "key_words": ("Lucas"),
        "room_description": "&wLucas meanders about aimlessly.&N",
        "description": ("A student with a faraway look,\n" "Or  just lost."),
        "race": "Elf",
        "class": "Shortone",
        "level": 1,
        "stats": [60, 65, 60, 80, 70, 75],
        "aggro": False,
        "wander": True,
    },
    "The_Inn_Maid": {
        "name": "Maudie, the inn's maid",
        "key_words": ("Maudie", "inn's", "maid"),
        "room_description": "&wMaudie, the inn's maid, cleans the inn thoroughly and happily.&N",
        "description": ("A nice lady with a smile on her face"),
        "race": "Human",
        "class": "Cleric",
        "level": 1,
        "stats": [60, 65, 60, 80, 70, 75],
        "aggro": False,
        "wander": True,
    },
    "Bob": {
        "name": "Bob",
        "key_words": ("Bob"),
        "room_description": "&bBob stands on the sidewalk talking to himself like a crazy person.&N",
        "description": ("A man who's known for being a local kook. But beneath his craziness is immense amounts of strength."),
        "race": "Human", 
        "class": "Barbarian",
        "level": 50,
        "stats": [100, 90, 100, 90, 99, 2],
        "aggro": False,
        "killable": True,
        "wander": False,
    },
    "Hatsune_Miku": {
        "name": "Hatsune Miku",
        "key_words": ("Hatsune", "Miku"),
        "room_description": "&bHatsune Miku stands here, being her normal diva self.&N",
        "description": ("A teen girl with long teal twin-tails and a futuristic black-and-teal school uniform"),
        "race": "Android",
        "class": "Vocaloid",
        "level": 50,
        "stats": [100, 90, 100, 90, 99, 100],
        "aggro": False,
        "killable": False,
        "wander": True,
        "responses": {
            "hi": ("&bHatsune Miku&Wlooks at you.&N",
                   "She says to you '&LOh, hi there! Do you want to come to my concert?&N'"),
            "no": ("&bShe begins to cry.&N",
                   "She says'&LOh, ok.&N"),
            "yes": ("&bHer&Weyes start to gleam with joy.&N",
                    "She says 'Great! It's at nine at the Tokyo Dome.&N'"),
            "loser": ("bHatsune Miku&Wlooks pissed.&N",
                      "She yells '&LOh, ok then! Be like that!.&N")
        }
    }
}


# Module-level spawn — rooms.py calls  M.spawn("void_guardian")
spawn = make_spawner(TEMPLATES, lambda: Mob)