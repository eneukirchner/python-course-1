#!/usr/bin/env python3
"""
 Rechtecke klassenbasiert zeichnen mit pygame
 Thanks to
 http://programarcadegames.com/index.php?chapter=lab_classes_and_graphics
"""
 
import pygame
from random import randint
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen size
SIZEX = 700;
SIZEY = 500

class Rectangle():
    """
    Rechteck-Klasse mit Farbe, Ort (x, y), Breite und Hoehe
    """
    def __init__(self, color, x, y, w, h):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.h, self.w])

    def move(self, delta_x, delta_y):
        if self.x + delta_x >= SIZEX - self.w or self.x + delta_x <= 0:
            delta_x *= -1
        if self.y + delta_y >= SIZEY -self.h or self.y + delta_y <= 0:
            delta_y *= -1
            
        self.x += delta_x
        self.y += delta_y
        
class Ellipse(Rectangle):
    """
    Ellipse-Klasse von Rectangle abgeleitet
    """

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.w, self.h])


def main():
    """
    Hauptprogramm mit game-Loop
    """
    my_list = []
    for i in range(10):
        x = randint(0, 600)
        y = randint(0, 400)
        h = randint(20, 50)
        w = randint(20, 50)
        col =[randint(0, 255), randint(0,255), randint(0,255)]
        my_object = Rectangle(col, x, y, h, w)
        my_list.append(my_object)
        
    for i in range(10):
        x = randint(0, 600)
        y = randint(0, 400)
        h = randint(20, 50)
        w = randint(20, 50)
        col =[randint(0, 255), randint(0,255), randint(0,255)]
        my_object = Ellipse(col, x, y, h, w)
        my_list.append(my_object)    
               
    pygame.init()
     
    # Set the width and height of the screen [width, height]
    size = (SIZEX, SIZEY)
    screen = pygame.display.set_mode(size)
     
    pygame.display.set_caption("Pygame Example")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
        # --- Game logic should go here
     
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(WHITE)
        for obj in my_list:
            obj.draw(screen)
            dx = randint(-3, 3)
            dy = randint(-3, 3)
            obj.move(dx, dy)
        # --- Drawing code should go here
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()

if __name__ == "__main__":
    main()

