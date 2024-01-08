import pygame
pygame.init()

from grid import Grid, START, END

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

        self.grid = Grid(0, 0, 800, 10)
        self.draw_mode = False
        self.earaser = False
        self.starting_square = []
        self.goal_square = []

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
                    elif not self.goal_square:

                        self.goal_square = self.grid.pos_to_index(self.get_mouse_pos())
                        self.grid.set_square(self.goal_square[0], self.goal_square[1], END)

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