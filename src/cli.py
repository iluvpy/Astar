from random import randint

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

    

def print_grid(grid):
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
array serves as an indicator to which nodes need to have their g, h and f costs to be calculated (to_search array).
for every step of the path finding algorithm (a step being the whole essential process that will be repeated until a path is found
or until no path was found).
Each element of that array (to_search) will be first sorted by the f cost and if there are multiple
nodes with the same minimal f cost they will be too sorted by the h cost, to find the best next node to check.
Once that best node has been found all nodes around that node will be each getting their g, h and f costs calculated based
on the path formed from that best node.
the best node will be removed from the 'unexplored' array and the new nodes that got their g and h costs calculated will 
get added to the unexplored array.

when a new best node gets found the best path needs to update, writing that should be easy having the basic
procedure written down

"""

class AstarAlgorithm:

    def __init__(self, width, height) -> None:
        start_j, start_i = [randint(0, width - 1), 
                            randint(0, height - 1)]
        goal_j, goal_i = [randint(0, width - 1), 
                          randint(0, height - 1)]
        self.grid = [[Node() for _ in range(width)] for _ in range(height)]
        self.start = self.grid[start_i][start_j]
        self.goal = self.grid[goal_i][goal_j]
        self.goal_index = [goal_i, goal_j]
        self.start.is_start = True
        self.goal.is_goal = True
        self.to_search = [[start_i, start_j]]

    def update(self) -> list:

        # find the index of the nodes with lowest f cost 
        f_costs = [self.grid[i][j].get_f() for i, j in self.to_search]
        min_f_cost = min(f_costs)
        print(f"min f cost: {min_f_cost}")
        f_cost_indexes = [] 
        for i, cost in enumerate(f_costs):
            if cost == min_f_cost:
                print(f"i: {i} and cost: {cost}")
                f_cost_indexes.append(i)
        print(f"to search: {self.to_search}")
        print(f"f cost indexes: {f_cost_indexes}")
        # if there are multiple nodes with the same minimal f_cost
        # then sort them again by lowest h_cost
        # get actual nodes from indexes
        i, j = self.to_search[f_cost_indexes[0]]
        lowest_h_cost = self.grid[i][j].h 
        best_node = self.to_search[0]
        if len(f_cost_indexes) > 1:
            for index in f_cost_indexes:
                i, j = self.to_search[index]
                h_cost = self.grid[i][j].h
                f_cost = self.grid[i][j].get_f()
                if h_cost < lowest_h_cost and f_cost == min_f_cost:
                    lowest_h_cost = h_cost
                    best_node = index

        print(f"best node: {best_node}")
        print(f"best node f cost: {self.grid[best_node[0]][best_node[1]].get_f()}")
        # calculate all costs for the nodes around best_node (3x3)
        # i, j starting pos
        # all the nodes around best_node will be added to the 
        bni, bnj = best_node
        starting_index = (bni - 1, bnj - 1) # the top left corner of the 3x3
        start_i, start_j = starting_index   
        for i in range(3):
            for j in range(3):
                node_i = start_i + i
                node_j = start_j + j
                if (node_i, node_j) != best_node and \
                        node_i >= 0 and node_j >= 0 and  \
                        node_i < len(self.grid) and \
                        node_j < len(self.grid[0]):
                    new_g_cost = 10 # horizontal or vertical g_cost
                    if (abs(i - 1) + abs(j - 1)) > 1: # diagonal g_cost
                        new_g_cost = 14

                    self.grid[node_i][node_j].g = new_g_cost
                    self.grid[node_i][node_j].h = abs(node_i - self.goal_index[0]) + abs(node_j - self.goal_index[1])
                    self.grid[node_i][node_j].explored = True
                    print(f"new g cost of node x {node_j}, y {node_i}: {new_g_cost}")
                    self.to_search.append([node_i, node_j])
        print(f"best node {best_node}")
        print("pre remove from unexplore")
        for i in range(len(self.to_search)):
            if self.to_search[i] == best_node:
                print(f"removed best node from to_search: {self.to_search[i]}")
                self.to_search.pop(i)
                break

        return best_node
    

def main():
    print("CLI A*:")
    width = 10
    height = 10
    astar = AstarAlgorithm(width, height)

    it = 0
    while True:
        print(f"iteration: {it}")
        print_grid(astar.grid)
 
        best_node = astar.update()
        if best_node == astar.goal_index:
            print("Found best path")
            break

        input_ = input("enter for next iteration...") 
        it += 1
        if input_ == "q":
            break

if __name__ == "__main__":
    main()