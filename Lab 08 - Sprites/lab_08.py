import arcade
import random

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "lab 8"

SPEED = 4

class Player(arcade.Sprite):

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0

        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0

        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Meteor(arcade.Sprite):

    def update(self, Meteor_speed = -2):
        self.Meteor_speed = random.randrange(-3, -1)
        self.center_y += self.Meteor_speed
        if self.center_y < -2200:
            self.center_y = 600


class Box(arcade.Sprite):

    def update(self, Meteor_speed = -2):
        self.Meteor_speed = random.randrange(-3, -1)
        self.center_y += self.Meteor_speed
        self.center_x += 2

        if self.center_y < -2200:
            self.center_y = 600

        if self.center_x > 800:
            self.center_x = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        arcade.set_background_color((0,0,40))

    def setup(self):

        bad_sprite_pngs = ["spaceMeteors_003.png", "spaceMeteors_001.png", "spaceMeteors_002.png",
"spaceMeteors_004.png", "spaceBuilding_015.png"]

        self.player_list = arcade.SpriteList()
        self.bad_list = arcade.SpriteList()
        self.good_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = Player("spaceShips_009.png", SPRITE_SCALING, angle = 180)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(35):
            self.meteor_sprites = Meteor(bad_sprite_pngs[random.randrange(0, 5)], 0.3)
            self.meteor_sprites.center_x = random.randrange(0, 800)
            self.meteor_sprites.center_y = random.randrange(650, 3400)
            self.bad_list.append(self.meteor_sprites)

        for i in range(15):
            self.box_sprite = Box("spaceBuilding_001.png", 0.5)
            self.box_sprite.center_x = random.randrange(0, 800)
            self.box_sprite.center_y = random.randrange(600, 3400)
            self.good_list.append(self.box_sprite)


    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.bad_list.draw()
        self.good_list.draw()

        arcade.draw_text("Score: " + str(self.score), 10, 20, arcade.color.WHITE, 14)

        if len(self.good_list) == 0:
            arcade.draw_text(("""GAME"""), 90, 350, arcade.color.WHITE, 150)
            arcade.draw_text(("""OVER"""), 90, 200, arcade.color.WHITE, 150)

    def on_update(self, delta_time):
        self.good_sound = arcade.load_sound("good.wav")
        self.bad_sound = arcade.load_sound("bad.wav")

        if len(self.good_list) != 0:
            self.player_list.update()
            self.bad_list.update()
            self.good_list.update()

        boxs_collected = arcade.check_for_collision_with_list(self.player_sprite, self.good_list)
        for box in boxs_collected:
            box.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.score += 1

        meteors_hit = arcade.check_for_collision_with_list(self.player_sprite, self.bad_list)
        for meteors in meteors_hit:
            meteors.remove_from_sprite_lists()
            arcade.play_sound(self.bad_sound)
            self.score -= 1


    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = SPEED



    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

main()