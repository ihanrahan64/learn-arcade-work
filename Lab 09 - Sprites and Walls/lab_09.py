import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 7


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
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)


    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        # Create a row of boxes
        for x in range(173, 650, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        # Create a column of boxes
        for y in range(-1200, 600, 64):
            wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png",
                                 SPRITE_SCALING)
            wall.center_x = 800
            wall.center_y = y
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()
        self.camera_sprites.use()
        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()

        self.camera_gui.use()
        arcade.draw_circle_filled(10, 10,1, arcade.color.RADICAL_RED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        if int(self.camera_sprites.position[0]) % 800 <= 7 and int(self.camera_sprites.position[1]) % 600 <= 7:
            self.physics_engine.update()

        self.scroll_to_player()

    def scroll_to_player(self):
        self.cam_x = 0
        self.cam_y = 0

        position = Vec2(self.cam_x, self.cam_y)
        if self.player_sprite.center_x < self.cam_x:
            self.cam_x -= 800
            if self.player_sprite.center_x < self.cam_x:
                self.cam_x -= 800
            position = Vec2(self.cam_x, self.cam_y)

        if self.player_sprite.center_y < self.cam_y:
            self.cam_y -= 600
            if self.player_sprite.center_y < self.cam_y:
                self.cam_y -= 600
            position = Vec2(self.cam_x, self.cam_y)


        self.camera_sprites.move_to(position, 0.125)


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()