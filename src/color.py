import pygame

class Color:
    def __init__(self, r, g, b, a=255) -> None:
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    # returns the pygame.Color object 
    def get(self):
        return pygame.Color(self.r, self.g, self.b, self.a)