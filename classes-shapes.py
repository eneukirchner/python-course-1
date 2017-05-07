#!/usr/bin/env python3
"""
Simple Class Example

"""

import arcade

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class Shape():

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class Ellipse(Shape):

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height,
                                   self.color)


class Rectangle(Shape):

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color,)


class MyApplication(arcade.Window):
    
    """ Main application class. """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()

        shape1 = Rectangle(200, 100, 200, 100, arcade.color.BLUE)
        shape2 = Ellipse(400, 300, 300, 100, arcade.color.RED)

        shape1.draw()
        shape2.draw()
        
window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT, title="Shapes!")
arcade.run()
