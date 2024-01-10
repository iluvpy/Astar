import pygame
pygame.init()

from grid import Grid, START, END

# # nodes = squares on grid
# class Node:
#     def __init__(self) -> None:
#         self.g = 0
#         self.h = 0
    
#     def get_f_value(self):
#         return self.g + self.h
    
# # the squares on the grid
# class Astar_algorithm:
#     def __init__(self, size) -> None:
#         # 2D list of nodes
#         self.grid = [[Node() for _ in range(size)] for _ in range(size)]
#         # the x, y index of the starting square
#         self.starting_pos = []
#         # the x, y index of the goal square
#         self.goal_pos = [] 
#         self.checked_squares = []
#         self.unexplored_positions = []

#     """
#         calculates the g, h, and f values of the square in index_pos, 
#         and also for every square around index_pos in a 1 square radius
#     """
#     def check_square(self, index_pos):
#         self.checked_squares.append(index_pos)
        
#         for i in range(3):
#             for j in range(3):
#                 if (j, i) != index_pos:
#                     self.grid[i][j].g = 
        

#     def calculate_gh(self, index_pos):
#         x, y = index_pos


#     def calculate_unexplored(self):
#         for square in self.unexplored_positions:
#             self.check_square(square)

#     def set_start(self, index_starting_pos):
#         self.starting_pos = index_starting_pos
#         self.unexplored_positions.append(index_starting_pos)
    
#     def set_goal(self, index_end_pos):
#         self.goal_pos = index_end_pos

#     def update(self):
#         pass

class Astar:
    def __init__(self) -> None:

        print(
        """
        The first two clicks will be the selecting the starting square (green) and the goal square (red) 
        and after that you'll be able to Left click to draw obstacles, 
        press 'r' to reset them and 'e' to activate earaser
        """)


        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Astar")

        self.grid = Grid(width=800, square_width=10)
        self.draw_mode = False
        self.earaser = False
        self.starting_square = []
        self.goal_square = []
        self.astar = Astar_algorithm(self.grid.get_grid_width_in_squares())

    def run(self):
        while True:
            quit_ = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_ = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.starting_square:
                        self.starting_square = self.grid.pos_to_index(self.get_mouse_pos())
                        self.grid.set_square(self.starting_square[0], self.starting_square[1], START)
                        self.astar.set_start(self.starting_square)
                    elif not self.goal_square:

                        self.goal_square = self.grid.pos_to_index(self.get_mouse_pos())
                        self.grid.set_square(self.goal_square[0], self.goal_square[1], END)
                        self.astar.set_goal(self.goal_square)

                    else:
                        self.draw_mode = True
                if event.type == pygame.MOUSEBUTTONUP:
                    self.draw_mode = False
                
                if event.type == pygame.KEYDOWN:
                    if self.starting_square and self.goal_square:
                        if event.key == pygame.K_r:
                            # reset all obstacles
                            self.grid.clear_squares() 
                            self.starting_square = []
                            self.goal_square = []
                        if event.key == pygame.K_e:
                            self.earaser = True
            if quit_:
                break

            
            self.draw()
            pygame.time.delay(10)

    def draw(self):
        self.screen.fill((255, 255, 255))
        mouse_pos = pygame.mouse.get_pos()

        if self.draw_mode:
            self.grid.click_square(mouse_pos)

        if self.earaser and self.draw_mode:
            self.grid.clear_square(mouse_pos)

        self.grid.draw(self.screen)
        pygame.display.update()

    def get_mouse_pos(self):
        return pygame.mouse.get_pos()

if __name__ == "__main__":
    app = Astar()
    app.run()
    pygame.quit()