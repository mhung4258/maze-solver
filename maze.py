from cell import *
import time

class Maze:

    def __init__(self, x,y, rows, cols, size, win):

        self._x = x
        self._y = y
        self._rows = rows
        self._cols = cols
        self._size = size
        self._win = win
        self._cells = []
        self._create_cells()

    
    # fill cells list with list of cells
    def _create_cells(self):
        y = self._y  
        for _ in range(self._rows):
            column = []
            x = self._x
            for _ in range(self._cols):
                cell = Cell(x,y,self._size,self._win)
                column.append(cell)
                x += self._size
            self._cells.append(column)
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
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)