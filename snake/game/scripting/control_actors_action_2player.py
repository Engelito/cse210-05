import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.control_actors_action import ControlActorsAction

class ControlActorsAction2Player(ControlActorsAction):
    """
    An input action that controls multiple snakes.
    
    The responsibility of ControlActorsAction is to get the direction and move both snake's heads.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """
    def __init__(self, keyboard_service):
        super().__init__(keyboard_service)
    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snake1 = cast.get_actors("snakes")[0]
        snake2 = cast.get_actors("snakes")[1] 

        "for snake 1:"

        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        # make sure the player isn't trying to turn the snake on itself
        if self._direction.equals(snake1.get_head().get_velocity().reverse()):
            snake1.turn_head(self._direction)
        

        "for snake 2:"

        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        # make sure the player isn't trying to turn the snake on itself
        if self._direction.equals(snake2.get_head().get_velocity().reverse()):
            snake2.turn_head(self._direction)
        

