from game.casting.snake import Snake
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Snake_blue(Snake):
    def __init__(self):
        super().__init__()
        self.set_color(constants.LBLUE)

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 4)

        position = Point(x * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "8"
        color = constants.BLUE

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)
