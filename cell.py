from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._x2 = None
        self._win = win

    def draw_wall(self, x1, y1, x2, y2, has_wall, color='white'):
        line = Line(Point(x1, y1), Point(x2, y2))
        self._win.draw_line(line, color if not has_wall else None)


    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.draw_wall(x1, y1, x1, y2, self.has_left_wall)
        self.draw_wall(x1, y1, x2, y1, self.has_top_wall)
        self.draw_wall(x2, y1, x2, y2, self.has_right_wall)
        self.draw_wall(x1, y2, x2, y2, self.has_bottom_wall)


    def calculate_center(self, x1, x2, y1):
        half_length = abs(x2 - x1) // 2
        x_center = half_length + x1
        y_center = half_length + y1
        return x_center, y_center

    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return

        fill_color = 'gray' if undo else 'red'

        x_center, y_center = self.calculate_center(self._x1, self._x2, self._y1)
        x_center2, y_center2 = self.calculate_center(to_cell._x1, to_cell._x2, to_cell._y1)

        self.draw_wall(x_center, y_center, x_center2, y_center2, False, fill_color)
