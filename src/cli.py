from random import randint


# handles the current path and new best paths of the search algorithm
class Path:
    def __init__(self) -> None:
        pass
        

class Node:
    def __init__(self) -> None:
        self.g = 0
        self.h = 0
        self.explored = False
        self.connections = [] # to other nodes

    def get_f(self):
        return self.g + self.h

    

def print_grid(grid, width):
    for node_list in grid:
        for node in node_list:
            print("#" if not node.explored else node.get_f(), end="")
        print() # endline


"""
Algorithm undestanding:
Note: squares and nodes are essentially the same thing in this case
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
    grid= [[Node() for _ in range(width)] for _ in range(height)]
    start = [randint(0, width - 1), randint(0, height - 1)]
    goal = [randint(0, width - 1), randint(0, height - 1)]

    unexplored = [start]
    explored = []
    while True:
        print_grid(grid, width)

        # find the index of lowest f cost nodes 
        f_values_unexplored = [grid[i][j].get_f() for j, i in unexplored]
        min_f_cost = min(f_values_unexplored)
        lowest_f_cost = []
        for f_cost, i in enumerate(f_values_unexplored):
            if f_cost == min_f_cost:
                lowest_f_cost.append(i)

        # if there are multiple nodes with the same minimal f_cost
        # then sort them again by lowest h_cost
        # get actual nodes from indexes
        j, i = unexplored[lowest_f_cost[0]]
        lowest_h_cost = grid[i][j].h 
        if len(lowest_f_cost) > 1:
            for index in lowest_f_cost:
                j, i = unexplored[lowest_f_cost[index]]
                h_cost = grid[i][j]
                if h_cost < lowest_h_cost:
                    lowest_fh_cost = h_cost


        # # calculate g and h costs of nodes around every unexplored node
        # for node_index in lowest_f_cost:
        #     explored.append(node_index)
        #     for i in range(3):
        #         for j in range(3):
        #             if (j, i) != node_index:
        #                 x, y = node_index
                        

        input_ = input("enter for next iteration...") 
        if input_ == "q":
            break

if __name__ == "__main__":
    main()