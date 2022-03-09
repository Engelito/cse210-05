from game.casting.snake import Snake
import constants
from game.casting.actor import Actor
from game.shared.point import Point

class Snake_red(Snake):

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
            segment.set_color(constants.RED)
            self._segments.append(segment)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        position = Point(x * constants.CELL_SIZE, y)
        velocity = Point(1 * constants.CELL_SIZE, 0)
        text = "8"
        color = constants.YELLOW

        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)

        # for i in range(constants.SNAKE_LENGTH):
        #     position = Point(x - i * constants.CELL_SIZE, y)
        #     velocity = Point(1 * constants.CELL_SIZE, 0)
        #     text = "8" if i == 0 else "#"
        #     color = constants.YELLOW if i == 0 else constants.RED
            
            # segment = Actor()
            # segment.set_position(position)
            # segment.set_velocity(velocity)
            # segment.set_text(text)
            # segment.set_color(color)
            # self._segments.append(segment)