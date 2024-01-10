from random import randint

class Node:
    def __init__(self) -> None:
        self.g = 0
        self.h = 0
        self.explored = False

    def get_f(self):
        return self.g + self.h

def print_grid(grid, width):
    for node_list in grid:
        for node in node_list:
            print("#" if not node.explored else node.get_f(), end="")
        print() # endline

def main():
    print("CLI A*:")
    width = 10
    height = 10
    grid = [[Node() for _ in range(width)] for _ in range(height)]
    start = [randint(0, width - 1), randint(0, height - 1)]
    goal = [randint(0, width - 1), randint(0, height - 1)]

    while True:
        print_grid(grid, width)

        

        input_ = input("enter for next iteration...") 
        if input_ == "q":
            break

if __name__ == "__main__":
    main()