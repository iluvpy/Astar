from __future__ import annotations

import pygame
from pprint import pprint
from typing import List, Dict
import math

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255) 
RED = (255, 0, 0)
GREY = (80, 80, 80)

class Node:
    def __init__(self, i, j, goal_pos) -> None:
        self.i = i
        self.j = j

        self.g_cost = 0
        self.h_cost = 0
        self.calculate_hcost(goal_pos)

        self.is_goal = False

        self.parent = None


    def calculate_hcost(self, goal_pos):
        self.h_cost = int(math.sqrt(((goal_pos[0] - self.i)*10)**2 + ((goal_pos[1] - self.j) * 10)**2))


    def get_neighbours(self, grid) -> List[Node]:
        grid_length_x = len(grid[0])
        grid_length_y = len(grid)
        neighbours = []
        # checking 3x3 like so
        #  |n|n|n|
        #  |n|s|n|
        #  |n|n|n|
        # where n stands for neighbour and s for self
        for i in range(self.i - 1, self.i+2):
            for j in range(self.j - 1, self.j + 2):
                # skip non existant neighbours (indexes outside of grid)
                # skip this node (self)
                if i < 0 or i >= grid_length_y:    
                    continue
                if j < 0 or j >= grid_length_x:
                    continue
                if (i, j) == (self.i, self.j):
                    continue
                neighbours.append(grid[i][j])
        return neighbours



    # add neighbours to priority queue, remove self from queue
    # find neighbour with lowest f-cost
    def explore_neighbours(self, grid: List[List[Node]], priority_queue: List[tuple], visited, goal_pos):
        grid_length_x = len(grid[0])
        grid_length_y = len(grid)
        neighbours: List[Node] = self.get_neighbours(grid)
        for neighbour in neighbours:
            neighbour.calculate_cost(self, goal_pos)
            ni, nj = neighbour.i, neighbour.j
            if (ni, nj) not in visited:
                if (ni, nj) not in priority_queue:
                    priority_queue.append((ni, nj))
                if (self.i, self.j) == goal_pos:
                    print("yay found goal")
                    exit()
        
        priority_queue.remove((self.i, self.j))
        visited.append((self.i, self.j))

    # calculate g cost with neighbour node g cost, if neighbour node is None, then this is the start Node, ie 0 g_cost
    # calculate h cost with goal pos
    def calculate_cost(self, neighbour_node: Node, goal_pos):
        self.parent = neighbour_node
        (di, dj) = (abs(self.i - self.parent.i), abs(self.j - self.parent.j)) # delta i, delta j
        self.g_cost = self.parent.g_cost
        if di == dj: # diagonal # when this node is diagonal to the parent node, then di, dj will be the same 
            self.g_cost += 14
        else: # when the change in di, dj is not the same, then the parent node is not diagonal do this node
            self.g_cost += 10
        self.calculate_hcost(goal_pos)
        
    def get_fcost(self):
        return self.g_cost + self.h_cost
    
    def is_in_priority(self, priority_queue):
        return (self.i, self.j) in priority_queue

    def __lt__(self, other: Node) -> bool:
        if self.get_fcost() == other.get_fcost():
            return self.h_cost < other.h_cost
        return self.get_fcost() < other.get_fcost()

    def __gt__(self, other: Node) -> bool:
        if self.get_fcost() == other.get_fcost():
            return self.h_cost > other.h_cost
        return self.get_fcost() > other.get_fcost()

class Grid:
    def __init__(self, screen_size, goal_pos, cell_size) -> None:
        # default cell size is 10 pixel
        self.cell_size = cell_size
        self.grid_width = screen_size[0]
        self.grid_height = screen_size[1]

        self.nodes: List[List[Node]] = []
        self.number_cells_y = int(self.grid_height / self.cell_size)
        self.number_cells_x = int(self.grid_width / self.cell_size)

        self.ticks = 0

        for i in range(self.number_cells_y):
            layer = []
            for j in range(self.number_cells_x):
                layer.append(Node(i, j, goal_pos))
            self.nodes.append(layer)
        


    def update(self, priority_queue, visited, goal_pos):
        # find best in priority queue (there could be more than one)
        priority_queue_nodes = [self.nodes[pos[0]][pos[1]] for pos in priority_queue]
        sorted_nodes = sorted(priority_queue_nodes)
        # last node will have the smallest fcost and g cost
        sorted_nodes[0].explore_neighbours(self.nodes, priority_queue, visited, goal_pos) 
        smallest_node = sorted_nodes[0]
 
        self.ticks += 1
        if self.ticks % 50 == 0: # remove nodes that are not needed

            print("hello checking every 50 ticks")
            priority_queue_nodes = [self.nodes[pos[0]][pos[1]] for pos in priority_queue]
            node: Node
            for node in priority_queue_nodes:
                neighbours: List[Node] = node.get_neighbours(self.nodes)
                neighbours_not_in_queue = sum([1 if not n.is_in_priority(priority_queue) else 0 for n in node.get_neighbours(self.nodes)])
                if neighbours_not_in_queue == 2:
                    print("removed node because no neighbours")
                    priority_queue.remove((node.i, node.j))

    def draw(self, screen):
        # vertical lines of grid
        for i in range(self.number_cells_x):
            pygame.draw.rect(screen, 
                             BLACK, 
                             (i * self.cell_size, 0, 1, self.grid_height))

        # horizontal lines of grid
        for i in range(self.number_cells_y):
            pygame.draw.rect(screen, 
                             BLACK, 
                             (0, i * self.cell_size, self.grid_width, 1))

def main():
    screen_size = (1920, 1080)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("A*")

    goal_node = (0, 100)
    grid = Grid(screen_size, goal_node, cell_size=20)
    start_node = (10, 0)
    priority_queue = [start_node]
    visited = []
    running = True
    while running:
        update_grid = False
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    update_grid = True
        if update_grid:
            grid.update(priority_queue, visited, goal_node)
        grid.draw(screen)

        for i in range(grid.number_cells_y):
            for j in range(grid.number_cells_x):
                if (i, j) in priority_queue:
                    pygame.draw.rect(screen, ORANGE, (j * grid.cell_size, i * grid.cell_size, grid.cell_size, grid.cell_size))
                if (i, j) in visited:
                    pygame.draw.rect(screen, GREY, (j * grid.cell_size, i * grid.cell_size, grid.cell_size, grid.cell_size))

        pygame.draw.rect(screen, BLUE, (start_node[1]* grid.cell_size, start_node[0]* grid.cell_size, grid.cell_size, grid.cell_size))
        pygame.draw.rect(screen, RED, (goal_node[1] * grid.cell_size, goal_node[0] * grid.cell_size, grid.cell_size, grid.cell_size))

        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()