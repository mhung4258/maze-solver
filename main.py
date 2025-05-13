from gui import *
from cell import *
from maze import * 

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 12
    m1 = Maze(50, 50, num_rows, num_cols, 30, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()