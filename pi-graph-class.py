#!/usr/bin/env python3
"""
Pi Monte Carlo with Classes
"""
import arcade
import random
import math

SCREEN_SIZE = 500

class MyApplication(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, point_size = 5):
        super().__init__(width, height)

        self.point_size = point_size
        self.x = 0
        self.y = 0
        self.r = 0
        arcade.set_background_color(arcade.color.WHITE)

        # Note:
        # You can change how often the animate() method is called by using the
        # set_update_rate() method in the parent class.
        # The default is once every 1/80 of a second.
        self.set_update_rate(2)
        arcade.start_render()
        
    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        # arcade.start_render()
        if self.r < 1:
            arcade.draw_point(self.x * SCREEN_SIZE, self.y * SCREEN_SIZE, arcade.color.RED, self.point_size)
        else:
            arcade.draw_point(self.x * SCREEN_SIZE, self.y * SCREEN_SIZE, arcade.color.BLUE, self.point_size)
        

    def animate(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        self.x = random.random()
        self.y = random.random()
        self.r = math.sqrt(self.x**2 + self.y**2)

window = MyApplication(SCREEN_SIZE, SCREEN_SIZE)

arcade.run()
