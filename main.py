import pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Node:
    def __init__(self, neighbours) -> None:
        self.neighbour = neighbours
        self.connected_width = None


class Grid:
    def __init__(self, w, h) -> None:
        # default cell size is 10 pixel
        self.cell_size = 10
        self.grid_width = w
        self.grid_height = h

        self.nodes = []
        self.vertical_cells = int(self.grid_height / self.cell_size)
        self.horizontal_cells = int(self.grid_width / self.cell_size)

    def update(self):
        pass

    def draw(self, screen):
        # vertical lines of grid
        for i in range(self.horizontal_cells):
            pygame.draw.rect(screen, 
                             BLACK, 
                             (i * self.cell_size, 0, 1, self.grid_height))

        # horizontal lines of grid
        for i in range(self.vertical_cells):
            pygame.draw.rect(screen, 
                             BLACK, 
                             (0, i * self.cell_size, self.grid_width, 1))

def main():
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("A*")

    grid = Grid(800, 600)

    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid.update()
        grid.draw(screen)

        pygame.display.update()



if __name__ == "__main__":
    main()
    pygame.quit()