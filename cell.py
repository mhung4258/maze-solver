from gui import *
class Cell:
    def __init__(
            self,x,y,size,window:Window, 
            has_left_wall = True, has_right_wall = True, 
            has_top_wall = True, has_bottom_wall = True
            ):
        self.x1 = x
        self.y1 = y
        self.x2 = x + size
        self.y2 = y + size
        self.size = size
        self.window = window

        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

        self.visited = False

    
    def draw(self):
        bg_color = self.window.canvas.cget("background")
        top_left = Point(self.x1,self.y1)
        top_right = Point(self.x2, self.y1)
        bottom_left = Point(self.x1, self.y2)
        bottom_right = Point(self.x2,self.y2)


        if self.has_top_wall:
            line = Line(top_left,top_right)
            self.window.draw_line(line)
        else:
            line = Line(top_left,top_right)
            self.window.draw_line(line, bg_color)
    
        if self.has_right_wall:
            line = Line(top_right, bottom_right)
            self.window.draw_line(line)
        else:
            line = Line(top_right, bottom_right)
            self.window.draw_line(line, bg_color)
        
        if self.has_bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.window.draw_line(line)
        else:
            line = Line(bottom_left, bottom_right)
            self.window.draw_line(line, bg_color)
        
        if self.has_left_wall:
            line = Line(top_left,bottom_left)
            self.window.draw_line(line)
        else:
            line = Line(top_left, bottom_left)
            self.window.draw_line(line, bg_color)

    
        
    # draws line between cells starting from the middle
    def draw_move(self, to_cell, undo = False):
        
        p1 = Point((self.x1 + self.x2)//2, (self.y1+self.y2)//2)
        p2 = Point((to_cell.x2 + to_cell.x1)//2, (to_cell.y2 + to_cell.y1)//2)

        line = Line(p1,p2)
        color = "gray" if undo else "red"
        self.window.draw_line(line, color)


        