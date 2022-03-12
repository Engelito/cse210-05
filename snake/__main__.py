import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.snake_red import Snake_red
from game.casting.snake_blue import Snake_blue
from game.scripting.script import Script
from game.scripting.control_actors_action_2player import ControlActorsAction2Player
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.two_snakes import HandleCollisionSecondSnake
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point



def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("snakes", Snake_red())
    # cast.add_actor("snakes", Snake())
    cast.add_actor("snakes", Snake_blue())

    score1 = Score()
    score1.set_position(Point(0, -1))
    cast.add_actor("scores", score1)

    score2 = Score()
    score2.set_position(Point(round(constants.MAX_X/2), -1))
    cast.add_actor("scores", score2)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction2Player(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionSecondSnake())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()