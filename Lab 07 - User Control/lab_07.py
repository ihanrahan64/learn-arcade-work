""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 2

class tree:
    def __init__(self, x, y, change_in_x, change_in_y):
        self.x = x
        self.y = y
        self.change_in_x = change_in_x
        self.change_in_y = change_in_y

    def draw(self):
        arcade.draw_line(self.x, self.y, self.x, self.y+25, arcade.color.PINK)
        arcade.draw_circle_filled(self.x, self.y, 13, arcade.color.GRAY)
        arcade.draw_triangle_filled(self.x-13, self.y-3, self.x+13, self.y-3, self.x, self.y-18, arcade.color.GRAY)
        arcade.draw_circle_filled(self.x-3, self.y-10, 2, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x+3, self.y-10, 2, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x, self.y-18, 3, arcade.color.BLACK)

    def restart(self):
        self.teleport = arcade.load_sound("tp.wav")
        self.x = 35
        self.y = 550
        arcade.play_sound(self.teleport)


    def update(self):
        self.hit_wall = arcade.load_sound("wall.wav")
        self.x += self.change_in_x
        if self.x >= SCREEN_WIDTH + 1:
            self.x = SCREEN_WIDTH - 10
            arcade.play_sound(self.hit_wall)

        if self.x <= -1:
            self.x = 10
            arcade.play_sound(self.hit_wall)

        self.y += self.change_in_y

        if self.y >= SCREEN_HEIGHT + 1:
            self.y = SCREEN_HEIGHT - 10
            arcade.play_sound(self.hit_wall)

        if self.y <= -1:
            self.y = 10
            arcade.play_sound(self.hit_wall)

        if 56 <= self.x <= 64 and self.y <= 400:
            self.restart()

        if 116 <= self.x <= 124 and 400 <= self.y <= 800:
            self.restart()

        if 120 <= self.x <= 180 and 400 <= self.y <= 408:
            self.restart()

        if 120 <= self.x <= 700 and 340 <= self.y <= 348:
            self.restart()

        if 176 <= self.x <= 184 and 60 <= self.y <= 348:
            self.restart()

        if 116 <= self.x <= 124 and 60 <= self.y <= 348:
            self.restart()

        if 176 <= self.x <= 184 and 0 <= self.y <= 348:
            self.restart()

        if 176 <= self.x <= 184 and 400 <= self.y <= 550:
            self.restart()

        if 696 <= self.x <= 704 and 60 <= self.y <= 348:
            self.restart()

        if 236 <= self.x <= 244 and 348 <= self.y <= 540:
            self.restart()

        if 300 <= self.x <= 800 and 396 <= self.y <= 404:
            self.restart()

        if 300 <= self.x <= 800 and 456 <= self.y <= 464:
            self.restart()

        if 636 <= self.x <= 644 and 0 <= self.y <= 348:
            self.restart()

class mouse:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, 40, 30, (0, 0, 0))
        arcade.draw_triangle_filled(self.x-20, self.y, self.x-5, self.y, self.x-15, self.y+25, (0, 0, 0))
        arcade.draw_triangle_filled(self.x+20, self.y, self.x+5, self.y, self.x+15, self.y+25, (0, 0, 0))
        arcade.draw_triangle_filled(self.x+3, self.y, self.x-3, self.y, self.x, self.y-3, arcade.color.PINK)
        arcade.draw_ellipse_filled(self.x-9, self.y+5, 3, 8, arcade.color.DARK_YELLOW)
        arcade.draw_ellipse_filled(self.x+9, self.y+5, 3, 8, arcade.color.DARK_YELLOW)





class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color((71, 41, 0))

        self.set_mouse_visible(False)

        self.Tree = tree(35, 550, 0, 0)
        self.Mouse = mouse(1, 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(60, 400, 60, 0, arcade.color.BLACK, 8)
        arcade.draw_line(120, 800, 120, 400, arcade.color.BLACK, 8)
        arcade.draw_line(120, 404, 180, 404, arcade.color.BLACK, 8)
        arcade.draw_line(180, 550, 180, 400, arcade.color.BLACK, 8)
        arcade.draw_line(700, 344, 120, 344, arcade.color.BLACK, 8)
        arcade.draw_line(120, 348, 120, 60, arcade.color.BLACK, 8)
        arcade.draw_line(180, 348, 180, 0, arcade.color.BLACK, 8)
        arcade.draw_line(700, 348, 700, 60, arcade.color.BLACK, 8)
        arcade.draw_line(240, 540, 240, 348, arcade.color.BLACK, 8)
        arcade.draw_line(300, 400, 800, 400, arcade.color.BLACK, 8)
        arcade.draw_line(300, 460, 800, 460, arcade.color.BLACK, 8)
        arcade.draw_line(640, 348, 640, 0, arcade.color.BLACK, 8)

        arcade.draw_triangle_filled(649,286, 669, 320, 679, 286, arcade.color.YELLOW)

        self.Tree.draw()
        self.Mouse.draw()

        print(str(self.Tree.x) + "  " + str(self.Tree.y))

    def update(self, delta_time):
        self.Tree.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.Mouse.x = x
        self.Mouse.y = y

    def on_mouse_press(self, x, y, button, modifiers):
        self.meow = arcade.load_sound("Cat 2.wav")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.Tree.x = 35
            self.Tree.y = 550
            arcade.play_sound(self.meow)


    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.Tree.change_in_x += -SPEED
        if key == arcade.key.RIGHT:
            self.Tree.change_in_x += SPEED
        if key == arcade.key.UP:
            self.Tree.change_in_y += SPEED
        if key == arcade.key.DOWN:
            self.Tree.change_in_y += -SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Tree.change_in_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.Tree.change_in_y = 0

def main():
    window = MyGame()
    arcade.run()


main()