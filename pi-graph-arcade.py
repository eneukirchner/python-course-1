#!/usr/bin/env python3
import random
import math
import arcade

# Konfiguration
SCREENSIZE = 500


# Funktionsdefinitionen
def draw_pi(delta):
    x = random.random()
    y = random.random()
    r = math.sqrt(x**2 + y**2)
    # Radius innerhalb des Kreises:
    if r < 1:
        arcade.draw_point(x * draw_pi.size, y * draw_pi.size, arcade.color.RED, 5)
        draw_pi.innen += 1
    else:
        arcade.draw_point(x * draw_pi.size, y * draw_pi.size, arcade.color.BLUE, 5)
    draw_pi.count += 1
    pi = 4 * draw_pi.innen / draw_pi.count
    # print("Pi = ", pi)

draw_pi.count = 0
draw_pi.innen = 0
draw_pi.size = SCREENSIZE
# Hauptprogramm
def main():
    
    DELAY = 1/100
    arcade.open_window("Test", SCREENSIZE, SCREENSIZE)
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    arcade.schedule(draw_pi, DELAY)
    arcade.run()
    
if __name__ == "__main__":
    main()
