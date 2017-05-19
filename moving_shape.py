#!/usr/bin/env python3
"""
Ball bounces with gravity
"""
import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
BOUNCINESS = 0.8
GRAVITY = 10


class MyApplication(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.ball_y_position = SCREEN_HEIGHT - BALL_RADIUS
        self.ball_y_pixels_per_second = 200

        arcade.set_background_color(arcade.color.BLACK)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        # self.set_update_rate(1/10)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Draw the circle
        arcade.draw_circle_filled(SCREEN_WIDTH // 2, self.ball_y_position,
                                  BALL_RADIUS, arcade.color.GREEN)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        self.ball_y_pixels_per_second = 200
        self.ball_y_position = SCREEN_HEIGHT - BALL_RADIUS

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        # Move the ball
        self.ball_y_position += self.ball_y_pixels_per_second * delta_time
        self.ball_y_pixels_per_second -= GRAVITY
        print("{:+8.2f}".format(self.ball_y_pixels_per_second))

        # Did the ball hit the right side of the screen while moving right?
        if self.ball_y_position > SCREEN_HEIGHT - BALL_RADIUS \
                and self.ball_y_pixels_per_second > 0:
            self.ball_y_pixels_per_second *= -BOUNCINESS

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_y_position < BALL_RADIUS \
                and self.ball_y_pixels_per_second < 0:
            self.ball_y_pixels_per_second *= -BOUNCINESS

        


def main():
    """ Main method """
    MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
 
