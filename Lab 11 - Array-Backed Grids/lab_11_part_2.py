import arcade

ROW_COUNT = 10
COLUMN_COUNT = 10


WIDTH = 20
HEIGHT = 20

MARGIN = 5

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):

    def __init__(self, width, height):

        super().__init__(width, height)

        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        arcade.start_render()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):

                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, modifiers):

        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0

        cells = 0
        for x in range(10):
            for y in range(10):
                if self.grid[x][y] == 1:
                    cells += 1
        print("there are " + str(cells) + " clicked")

        for x in range(10):
            row_cells = 0
            continuous_count = 0
            for y in range(10):
                if self.grid[x][y] == 1:
                    row_cells += 1
                    continuous_count += 1
                else:
                    if continuous_count >= 2:
                        print("There are " + str(continuous_count) + " continuous blocks selected on row " + str(x))
                    continuous_count = 0
                if y == 9 and continuous_count >= 2:
                        print("There are " + str(continuous_count) + " continuous blocks selected on row " + str(x))

            print("in row " + str(x) + " there are " + str(row_cells) + " clicked")

        for x in range(10):
            column_cells = 0
            for y in range(10):
                if self.grid[y][x] == 1:
                    column_cells += 1
            print("in column " + str(x) + " there are " + str(column_cells) + " clicked")
        print("")



def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()