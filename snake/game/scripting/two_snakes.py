from game.scripting.handle_collisions_action import HandleCollisionsAction

class HandleCollisionSecondSnake(HandleCollisionsAction):
    def _handle_segment_collision(self, cast):
        snake1 = cast.get_actors("snakes")[0]
        snake2 = cast.get_actors("snakes")[1]
        
        head1 = snake1.get_segments()[0]
        segments1 = snake1.get_segments()[1:]

        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        
        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                