from graphics import Line, Point


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win


    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            top_left = Point(x1, y1)
            bottom_left = Point(x1, y2)
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall)
        else:
            top_left = Point(x1, y1)
            bottom_left = Point(x1, y2)
            left_wall = Line(top_left, bottom_left)
            self._win.draw_line(left_wall, "white")

        if self.has_top_wall:
            top_left = Point(x1, y1)
            top_right = Point(x2, y1)
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall)
        else:
            top_left = Point(x1, y1)
            top_right = Point(x2, y1)
            top_wall = Line(top_left, top_right)
            self._win.draw_line(top_wall, "white")

        if self.has_right_wall:
            top_right = Point(x2, y1)
            bottom_right = Point(x2, y2)
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall)
        else:
            top_right = Point(x2, y1)
            bottom_right = Point(x2, y2)
            right_wall = Line(top_right, bottom_right)
            self._win.draw_line(right_wall, "white")

        if self.has_bottom_wall:
            bottom_right = Point(x2, y2)
            bottom_left = Point(x1, y2)
            bottom_wall = Line(bottom_right, bottom_left)
            self._win.draw_line(bottom_wall)
        else:
            bottom_right = Point(x2, y2)
            bottom_left = Point(x1, y2)
            bottom_wall = Line(bottom_right, bottom_left)
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        self.centre_x = (self._x1 + self._x2) / 2
        self.centre_y = (self._y1 + self._y2) / 2
        self.centre = Point(self.centre_x, self.centre_y)
        to_cell_centre_x = (to_cell._x1 + to_cell._x2) / 2
        to_cell_centre_y = (to_cell._y1 + to_cell._y2) / 2
        to_cell_centre = Point(to_cell_centre_x, to_cell_centre_y)

        if not undo:
            self._win.draw_line(Line(self.centre, to_cell_centre), "red")
        else:
            self._win.draw_line(Line(self.centre, to_cell_centre), "gray")
