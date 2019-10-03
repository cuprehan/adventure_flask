from route_helper import simple_route

GAME_HEADER = """
<h1>Welcome to monster hunter!</h1>
<p>At any time you can <a href='/reset/'>reset</a> your game.</p>
"""


@simple_route('/')
def hello(world: dict) -> str:
    """
    The welcome screen for the game.

    :param world: The current world
    :return: The HTML to show the player
    """
    return GAME_HEADER + """You are in the Lair of Monsters.<br>
    
    <a href="goto/lair one">Go further into the lair.</a>"""


@simple_route('/lair_one')
def start(world: dict, where: str) -> str:
    """
    <a href="goto/lair two">Proceed past lair one.</a>"""
    world['location'] = where
    return GAME_HEADER + "You are in lair 2.</br>"


@simple_route('/lair_two')
def middle(world: dict, where: str) -> str:
    """
    <a href="goto/lair three">Go to the end of the lair.</a>"""
    world['location'] = where
    return GAME_HEADER + "You are in lair 3.</a>"


ENCOUNTER_MONSTER = """
<!-- Curly braces let us inject values into the string -->
You are in {}. You found a monster!<br>

<!-- Image taken from site that generates random Corgi pictures-->
<img src="http://placecorgi.com/260/180" /><br>
    
What is its name?

<!-- Form allows you to have more text entry -->    
<form action="/save/name/">
    <input type="text" name="player"><br>
    <input type="submit" value="Submit"><br>
</form>
"""


@simple_route('/goto/<where>/')
def open_door(world: dict, where: str) -> str:
    """
    Update the player location and encounter a monster, prompting the player
    to give them a name.

    :param world: The current world
    :param where: The new location to move to
    :return: The HTML to show the player
    """
    world['location'] = where
    return GAME_HEADER + ENCOUNTER_MONSTER.format(where)


@simple_route("/save/name/")
def save_name(world: dict, monsters_name: str) -> str:
    """
    Update the name of the monster.

    :param world: The current world
    :param monsters_name:
    :return:
    """
    world['name'] = monsters_name

    return GAME_HEADER + """You are in {where}, and you are nearby {monster_name}
    <br><br>
    <a href='/'>Proceed further into the lair</a>
    """.format(where=world['location'], monster_name=world['name'])
