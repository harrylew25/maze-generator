from graphics import Window
from maze import Maze
import sys

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10_000)
    win = Window(screen_x, screen_y)
    
    maze = Maze(
        margin, 
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        100
    )
    print('Maze created')
    is_solvable = maze.solve()
    msg = 'maze solved' if is_solvable else 'maze cannot be solved'
    print(msg)

    win.wait_for_close()

main()