import pygame

GRAY = (100, 100, 100)
GREEN = (50, 255, 50)
RED = (255, 50, 50)

OBSTACLE = 1
START = 2
END = 3

class Grid:
    def __init__(self, x, y, width, square_width) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.square_width = square_width
        self.num_squares = width // square_width
        self.line_width = int(self.square_width * 0.1)
        self.squares = []
        self.clear_squares()

    def draw(self, screen):

        # vertical lines
        for i in range(self.num_squares):
            start = (self.x + i*self.square_width, 0)
            end = (self.x + i*self.square_width, self.width)
            self.draw_line(screen, start, end)

        # horizontal lines
        for i in range(self.num_squares):
            start = (0, self.y + i*self.square_width)
            end = (self.width, self.x + i*self.square_width)
            self.draw_line(screen, start, end)

        for i in range(self.num_squares):
            for j in range(self.num_squares):
                color = None
                square_val = self.squares[i][j]
                if square_val == OBSTACLE:
                    color = GRAY
                elif square_val == START:
                    color = GREEN
                elif square_val == END:
                    color = RED
                if color is not None:
                    x = j * self.square_width
                    y = i * self.square_width
                    self.draw_square(screen, x, y, color)

    def draw_line(self, screen, start, end):
        pygame.draw.line(screen, (0, 0, 0), start, end, width=self.line_width)

    def draw_square(self, screen, x, y, color):
        x += self.line_width
        y += self.line_width
        width = self.square_width - self.line_width
        pygame.draw.rect(screen, color, (x, y, width, width))

    def click_square(self, pos):
        i_x, i_y = self.pos_to_index(pos)
        self.squares[i_y][i_x] = 1
    
    def clear_squares(self):
        self.squares = [[0 for _ in range(self.num_squares)] for _ in range(self.num_squares)]
    
    def clear_square(self, pos):
        i_x, i_y = self.pos_to_index(pos)
        self.squares[i_y][i_x] = 0
    
    def pos_to_index(self, pos):
        x = pos[0]
        y = pos[1]
        if (x > self.width or x < 0) or (y > self.width or y < 0):
            print("couldn't find pixel")
            return 
        return x // self.square_width, y // self.square_width
    

    def set_square(self, i_x, i_y, value):
        self.squares[i_y][i_x] = value