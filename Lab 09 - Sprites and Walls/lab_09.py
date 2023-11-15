import arcade
import random
from pyglet.math import Vec2

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 21

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        self.cam_x = 0
        self.cam_y = 0

        # Sprite lists
        self.chest_list = None
        self.wall_list = None
        self.player_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.score = 0

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.chest_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        self.chest_sprite = arcade.Sprite("tile_0092.png", 4)
        self.chest_sprite.center_x = -650
        self.chest_sprite.center_y = 150
        self.chest_list.append(self.chest_sprite)

        self.coins = [1850, 470, -125, 1100, 1850, 970, -650, 700, 400, 1350]
        for x in range(0, len(self.coins), 2):
            self.coin_sprite = arcade.Sprite("tile_0092.png", 2)
            self.coin_sprite.center_x = self.coins[x]
            self.coin_sprite.center_y = self.coins[x+1]
            self.coin_list.append(self.coin_sprite)

        self.ghost_wall = arcade.Sprite("tile_0020.png", 3.16)


        self.row(-800, 2401, 0)
        self.row(-800, 2401, 1800)
        self.column(0, 1801, 2400)
        self.column(0,1801, -800)

        self.row(0, 556, 375)
        self.row(-800, -520, 350)
        self.row(0, 555, 600)
        self.row(950, 2001, 600)
        self.row(800, 951, 900)
        self.row(-200, 2001, 1200)
        self.row(800, 2001, 350)
        self.row(1400,2001, 1500)
        self.row(300, 1100, 1500)


        self.column(25,351, 550)
        self.column(0,1201,-250)
        self.column(350, 1201,-520)
        self.column(600,801, 0)
        self.column(400, 601, 800)
        self.column(600, 901, 950)
        self.column(600, 1201, 2000)
        self.column(1200,1501, 1400)
        self.column(1200,1501, 300)
        self.column(350,601, 2000)



        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

    def floor(self):
        for x in range(-800, 2401, 72):
            for y in range(0, 1801, 324):
                arcade.draw_lrtb_rectangle_filled(x, x + 69,y+321,y,(38,27,15))


    def row(self,start_x, end_x, y):
        self.walls = ["tile_0019.png", "tile_0040.png", "tile_0002.png"]
        for x in range(start_x, end_x, 50):
            if y == 0 or y == 1800:
                block = 2
            elif x % 7 == 0:
                block = 0
            else:
                block = 1

            if y == 0:
                wall = arcade.Sprite(self.walls[block], 3.16, flipped_vertically = True)
            else:
                wall = arcade.Sprite(self.walls[block],3.16)
            wall.center_x = x
            wall.center_y = y
            self.wall_list.append(wall)

    def column(self, start_y, end_y, x):
        self.walls = ["tile_0019.png", "tile_0040.png", "tile_0002.png"]
        for y in range(start_y, end_y, 50):
            if x == -800 or x == 2400:
                block = 2
            elif y % 7 == 0:
                block = 0
            else:
                block = 1

            if x == -800 or x == 2400:
                if x == -800:
                    wall = arcade.Sprite(self.walls[block], 3.16, angle=90)
                    wall.center_x = x
                    wall.center_y = y

                if x == 2400:
                        wall = arcade.Sprite(self.walls[block], 3.16, angle=-90)
                        wall.center_x = x
                        wall.center_y = y
            else:
                wall = arcade.Sprite(self.walls[block], 3.16)
                wall.center_x = x
                wall.center_y = y
            self.wall_list.append(wall)


    def on_draw(self):
        self.clear()

        self.camera_sprites.use()

        self.floor()
        self.wall_list.draw()
        self.player_list.draw()
        self.chest_list.draw()
        self.coin_list.draw()

        for x in range (2):
            self.ghost_wall.center_x = 850+50*x
            self.ghost_wall.center_y = 600
            self.ghost_wall.draw()


        self.camera_gui.use()

        arcade.draw_text("Score: " + str(self.score), 10, 20, arcade.color.WHITE, 14)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):

        self.good_sound = arcade.load_sound("good - Copy.wav")

        if ((int(self.camera_sprites.position[0]) % 800 <= 9 or int(self.camera_sprites.position[0]) % 800 >= 791)
                and (int(self.camera_sprites.position[1]) % 600 <= 9 or int(self.camera_sprites.position[1]) % 600 >= 591)):
            self.physics_engine.update()

        self.scroll_to_player()

        treasure_collected = arcade.check_for_collision_with_list(self.player_sprite, self.chest_list)
        for chest in treasure_collected:
            chest.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.score += 10

        coins_collected = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_collected:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.score += 1

    def scroll_to_player(self):

        if self.player_sprite.center_x < self.cam_x:
            self.cam_x -= 800

        if self.player_sprite.center_x > self.cam_x + 800:
            self.cam_x += 800

        if self.player_sprite.center_y < self.cam_y:
            self.cam_y -= 600

        if self.player_sprite.center_y > self.cam_y + 600:
            self.cam_y += 600


        position = Vec2(self.cam_x, self.cam_y)


        self.camera_sprites.move_to(position, 0.125)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()