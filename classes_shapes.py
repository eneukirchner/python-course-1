#!/usr/bin/env python3
"""
Simple Class Example

"""

import arcade

# Set up the constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class Shape():
    """ Base Class for all shapes """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color


class Ellipse(Shape):
    """ Ellipse Class """

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.width, self.height,
                                   self.color)


class Rectangle(Shape):
    """ Rectangle Class """

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height,
                                     self.color,)


class MyApplication(arcade.Window):
    
    """ Main application class. """
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.shape_list = []

    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        
        self.shape_list.append(Rectangle(200, 100, 200, 100, arcade.color.BLUE))
        self.shape_list.append(Ellipse(400, 300, 300, 100, arcade.color.RED))
        self.shape_list.append(Ellipse(500, 500, 100, 50, arcade.color.GREEN))

        for shape in self.shape_list:
            shape.draw()
        
def main():
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT, title="Shapes!")
    arcade.run()

if __name__ == "__main__":
    main()


