from random import randint
from pprint import pprint

# handles the current path and new best paths of the search algorithm
class Path:
    def __init__(self) -> None:
        pass
        

class Node:
    def __init__(self) -> None:
        self.g = 0 # g_cost
        self.h = 0 # h_cost 
        self.explored = False
        self.connections = [] # to other nodes
        self.is_start = False
        self.is_goal = False

    def get_f(self):
        return self.g + self.h

    

def print_grid(grid, width):
    for node_list in grid:
        for node in node_list:
            sign = " # "
            if node.explored:
                sign = f" {node.get_f()} "
            if node.is_start:
                sign = " S "
            if node.is_goal:
                sign = " G "
            print(sign, end="")
        print() # endline
    


"""
Algorithm undestanding:
Note: squares and nodes are the same thing in this case
theres a starting node (start) and a goal node (goal),
I start out with an array containing only the start node, that 
array serves as an indicator to which nodes need to have their g, h and f costs to be calculated.
for every step of the path finding algorithm (a step being the whole essential process that will be repeated until a path is found
or until no path was found)
each element of that list (unexplored) will be first sorted by the f cost and if there are multiple
nodes with the same minimal f cost they will be too sorted by the h cost, to find the best next node to check.
Once that best node has been found all nodes around that node will be each getting their g, h and f costs calculated based
on the path formed from that best node.
the best node will be removed from the 'unexplored' list and the new nodes that got their g and h costs calculated will 
get added to the unexplored list.

when a new best node gets found the best path needs to update, writing that should be easy having the basic
procedure written down

"""

def main():
    print("CLI A*:")
    width = 10
    height = 10
    grid = [[Node() for _ in range(width)] for _ in range(height)]
    start = [randint(0, width - 1), randint(0, height - 1)]
    goal = [randint(0, width - 1), randint(0, height - 1)]

    grid[start[0]][start[1]].is_start = True
    grid[goal[0]][goal[1]].is_goal = True

    unexplored = [start]
    explored = []
    it = 0
    while True:
        print(f"iteration: {it}")
        print_grid(grid, width)

        # find the index of lowest f cost nodes 
        f_values_unexplored = [grid[i][j].get_f() for i, j in unexplored]
        min_f_cost = min(f_values_unexplored)
        lowest_f_cost = [] 
        for i, f_cost in enumerate(f_values_unexplored):
            if f_cost == min_f_cost:
                lowest_f_cost.append(i)

        # if there are multiple nodes with the same minimal f_cost
        # then sort them again by lowest h_cost
        # get actual nodes from indexes
        i, j = unexplored[lowest_f_cost[0]]
        lowest_h_cost = grid[i][j].h 
        best_node = unexplored[0]
        if len(lowest_f_cost) > 1:
            for index in lowest_f_cost:
                i, j = unexplored[index]
                h_cost = grid[i][j].h
                if h_cost < lowest_h_cost:
                    lowest_h_cost = h_cost
                    best_node = index

        # calculate all costs for the nodes around best_node (3x3)
        # i, j starting pos
        bni, bnj = best_node
        starting_index = (bni - 1, bnj - 1) # the top left corner of the 3x3
        start_i, start_j = starting_index   
        for i in range(3):
            for j in range(3):
                node_i = start_i + i
                node_j = start_j + j
                if (node_i, node_j) != best_node and node_i >= 0 and node_j >= 0 and  \
                    node_i < len(grid) and node_j < len(grid[0]):
                    new_g_cost = 10 # horizontal or vertical g_cost
                    if (abs(i - 1) + abs(j - 1)) > 1: # diagonal g_cost
                        new_g_cost = 14

                    grid[node_i][node_j].g = new_g_cost
                    grid[node_i][node_j].h = abs(node_i - goal[0]) + abs(node_j - goal[1])
                    grid[node_i][node_j].explored = True
                    print(f"new g cost of node x {node_j}, y {node_i}: {new_g_cost}")
                    unexplored.append([node_i, node_j])
        print("pre remove from unexplore")
        unexplored.remove(best_node) 

        if best_node == goal:
            print("Found best path")
            break

        input_ = input("enter for next iteration...") 
        it += 1
        if input_ == "q":
            break

if __name__ == "__main__":
    main()