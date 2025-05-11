from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x=0,y=0):
        self._x = x
        self._y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas: Canvas, fill_color: str):
         canvas.create_line(
             self._p1._x, self._p1._y, self._p2._x,self._p2._y, fill=fill_color, width=2
         )


class Window:
    def __init__(self, width, height):

        self.root = Tk()
        self.root.title("Maze Solver")

        self.canvas = Canvas(self.root,height=height, width=width )
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        
    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str = 'black'):
        line.draw(self.canvas, fill_color)

