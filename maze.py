from cell import Cell
import random
import time
from tkinter import Tk, BOTH, Canvas, TclError

class Maze:

    def __init__(self, x,y, rows, cols, size, win, seed = None):

        self._x = x
        self._y = y
        self._rows = rows
        self._cols = cols
        self._size = size
        self._win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.solve()

    # fill cells list with list of cells
    def _create_cells(self):
        y = self._y  
        for i in range(self._rows):
            row_cells = []
            x = self._x
            for j in range(self._cols):
                cell = Cell(x,y,self._size,self._win)
                row_cells.append(cell)
                x += self._size
            self._cells.append(row_cells)
            y += self._size

        ## call the draw
        self._draw_cells()


    # draws all the cells based on i,j and cell size and x-y position of cells themselves
    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
        self._animate()

    def _animate(self):
        if self._win is None or not self._win.running:
            exit()
        try:
            self._win.redraw()
            time.sleep(0.01)
        except TclError:
            exit()


    def _break_entrance_and_exit(self):
        entrance = self._cells[0][0]
        exit = self._cells[self._rows-1][self._cols-1]

        entrance.has_top_wall = False
        entrance.draw()

        exit.has_bottom_wall = False
        exit.draw()

        self._animate()

    def _break_walls_r(self, i , j):
        curr = self._cells[i][j]
        curr.visited = True

        while True:
            to_visit = []
            #check adjacent cells to visit
            
            if i > 0 and not self._cells[i - 1][j].visited:  # up
                to_visit.append(('up', i - 1, j))
            if i < self._rows - 1 and not self._cells[i + 1][j].visited:  # down
                to_visit.append(('down', i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:  # left
                to_visit.append(('left', i, j - 1))
            if j < self._cols - 1 and not self._cells[i][j + 1].visited:  # right
                to_visit.append(('right', i, j + 1))

            if not to_visit:
                curr.draw()
                self._animate()
                return
        
            #random dir
            direction, r_i, r_j = random.choice(to_visit)
            visit = self._cells[r_i][r_j]

            #knock down the wall
            if direction == 'up':
                curr.has_top_wall = False
                visit.has_bottom_wall = False
            elif direction == 'down':
                curr.has_bottom_wall = False
                visit.has_top_wall = False
            elif direction == 'left':
                curr.has_left_wall = False
                visit.has_right_wall = False
            elif direction == 'right':
                curr.has_right_wall = False
                visit.has_left_wall = False

            self._break_walls_r(r_i,r_j)

    #resets all the visited property of all the cells in the mase to False
    def _reset_cells_visited(self):
        for i in range(self._rows):
            for j in range(self._cols):
                self._cells[i][j].visited = False

    def solve(self):
       return self._solve_r(0,0)


    def _solve_r(self, i , j):
        self._animate()
        curr = self._cells[i][j]
        curr.visited = True

        if curr == self._cells[self._rows-1][self._cols-1]:
            return True
        
        directions = [
            ('up', i-1,j, not curr.has_top_wall),
            ('down', i+1,j,not curr.has_bottom_wall),
            ('left', i, j - 1, not curr.has_left_wall),
            ('right', i, j + 1, not curr.has_right_wall)
        ]

        for direction, next_i, next_j, move in directions:
            if 0 <= next_i < self._rows and 0 <= next_j < self._cols and move:
                next_cell = self._cells[next_i][next_j]
                if not next_cell.visited:
                    curr.draw_move(next_cell)
                    if self._solve_r(next_i, next_j):
                        return True
                    
                    curr.draw_move(next_cell, undo = True)
        return False