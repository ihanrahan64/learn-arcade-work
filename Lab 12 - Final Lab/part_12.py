import arcade
import random
from pyglet.math import Vec2


UP = 1
DOWN = -2
LEFT = -3
RIGHT = 4

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Lab 9"

MOVEMENT_SPEED = 4


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.cam_x = 0
        self.cam_y = 0

        # Sprite lists
        self.chest_list = None
        self.wall_list = None
        self.player_list = None
        self.coin_list = None
        self.enemy_list = None
        self.weapon_list = None
        self.key_list = None
        self.staff_list = None
        self.door_list = None
        self.boss_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

        self.score = 0
        self.enemys_defeated = 0
        self.gold_collected = 0

        self.camera_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def player_setup(self):
        self.player_sprite = arcade.Sprite("tile_0096.png", 3)
        self.player_sprite.center_x = 500
        self.player_sprite.center_y = 315
        self.hp = 3
        self.player_list.append(self.player_sprite)

    def chest_setup(self):
        self.chest_sprite = arcade.Sprite("tile_0010.png", 4)
        self.chest_sprite.center_x = 2780
        self.chest_sprite.center_y = 2450.5
        self.chest_list.append(self.chest_sprite)

    def coin_setup(self):
        self.coins = [1500, 400, 1300, 3875, 1700, 3875, 2800, 2950, 3800, 1950, 4500, 3180]
        for x in range(0, len(self.coins), 2):
            self.coin_sprite = arcade.Sprite("tile_0005.png", 3)
            self.coin_sprite.center_x = self.coins[x]
            self.coin_sprite.center_y = self.coins[x + 1]
            self.coin_list.append(self.coin_sprite)

    def enemy_setup(self):
        #enemy 0
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 2500
        self.enemy_sprite.center_y = 400
        self.enemy_list.append(self.enemy_sprite)

        #enemy 1
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 1200
        self.enemy_sprite.center_y = 2250
        self.enemy_list.append(self.enemy_sprite)

        #enemy 2
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 2700
        self.enemy_sprite.center_y = 1850
        self.enemy_list.append(self.enemy_sprite)

        #enemy 3
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 1500
        self.enemy_sprite.center_y = 1750
        self.enemy_list.append(self.enemy_sprite)

        #enemy 4
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 3300
        self.enemy_sprite.center_y = 1950
        self.enemy_list.append(self.enemy_sprite)

        #enemy 5
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 3700
        self.enemy_sprite.center_y = 1550
        self.enemy_list.append(self.enemy_sprite)

        #enemy 6
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 2500
        self.enemy_sprite.center_y = 2950
        self.enemy_list.append(self.enemy_sprite)

        #enemy 7
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 3500
        self.enemy_sprite.center_y = 3800
        self.enemy_list.append(self.enemy_sprite)

        #enemy 8
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 3900
        self.enemy_sprite.center_y = 3900
        self.enemy_list.append(self.enemy_sprite)

        #enemy 9
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 3800
        self.enemy_sprite.center_y = 3280
        self.enemy_list.append(self.enemy_sprite)

        #enemy 10
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 3200
        self.enemy_sprite.center_y = 3280
        self.enemy_list.append(self.enemy_sprite)

        #enemy 11
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 10000
        self.enemy_sprite.center_y = 3280
        self.enemy_list.append(self.enemy_sprite)

        #enemy 12
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 4)
        self.enemy_sprite.center_x = 100000
        self.enemy_sprite.center_y = 3280
        self.enemy_list.append(self.enemy_sprite)

        #boss
        self.enemy_sprite = arcade.Sprite("tile_0109.png", 6)
        self.enemy_sprite.center_x = 3190
        self.enemy_sprite.center_y = 2438
        self.boss_list.append(self.enemy_sprite)

    def wepon_setup(self):
        self.sword_sprite = arcade.Sprite("tile_0104.png", 3.2)
        self.sword_sprite.center_x = 0
        self.sword_sprite.center_y = -100
        self.sword_sprite.angle = 0
        self.weapon_list.append(self.sword_sprite)

        self.arrow_sprite = arcade.Sprite("tile_0008.png", 3.2)
        self.arrow_sprite.center_x = 0
        self.arrow_sprite.center_y = -100
        self.arrow_sprite.angle = 0
        self.weapon_list.append(self.arrow_sprite)

    def setup(self):
        self.pointing = UP
        self.track_list_x = []
        self.track_list_y = []
        self.sword_timer = 0
        self.sword_check = False
        self.hit_timer = 0
        self.bow_timer = 0
        self.arrow_start_x = 0
        self.arrow_start_y = 0
        self.pointing_at_shot = 0
        self.door = True
        self.wand = False
        self.win = False
        self.boss_hp = 5
        self.boss_timer = -1


        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.chest_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.weapon_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()
        self.staff_list = arcade.SpriteList()
        self.door_list = arcade.SpriteList()
        self.boss_list = arcade.SpriteList()

        self.player_setup()
        self.chest_setup()
        self.coin_setup()
        self.enemy_setup()
        self.wepon_setup()

        for x in range(0, 151, 50):
            self.door_sprite = arcade.Sprite("tile_0003.png", 3)
            self.door_sprite.center_x = 4425+x
            self.door_sprite.center_y = 2830
            self.door_list.append(self.door_sprite)

        self.key_sprite = arcade.Sprite("tile_0000.png", 3.2)
        self.key_sprite.center_x = 1130
        self.key_sprite.center_y = 1770
        self.key_list.append(self.key_sprite)

        self.heart_sprite1 = arcade.Sprite("tile_0006.png", 2)
        self.heart_sprite1.center_x = 20
        self.heart_sprite1.center_y = 650

        self.heart_sprite2 = arcade.Sprite("tile_0006.png", 2)
        self.heart_sprite2.center_x = 50
        self.heart_sprite2.center_y = 650

        self.heart_sprite3 = arcade.Sprite("tile_0006.png", 2)
        self.heart_sprite3.center_x = 80
        self.heart_sprite3.center_y = 650

        self.staff_sprite = arcade.Sprite("tile_0009.png", 2)
        self.staff_sprite.center_x = 1500
        self.staff_sprite.center_y = 3875
        self.staff_list.append(self.staff_sprite)

        self.room(500, 350, right_door= True)
        self.room(1500, 350, True, True)
        self.room(2500, 350, True, True)

        self.room(500, 3150, right_door=True)
        self.room(1500, 3150, True, True, False, True)
        self.room(1500, 2450, up_door=True, right_door=True)
        self.room(2500, 2450, down_door=True, left_door=True ,right_door= True)
        self.room(2500, 1750, up_door=True, right_door=True, left_door=True)
        self.room(1500, 1750, right_door=True)
        self.room(3500, 1750, left_door=True)
        self.room(2500, 3150, True, up_door=True)
        self.room(2500, 3850, True, True, False, True)
        self.room(1500, 3850, right_door=True)
        self.room(4500, 3150, True, down_door=True)
        self.room(4500, 2450, True, up_door=True)
        self.room(3500, 2450, True, True)

        self.row(3025, 4000, 4175)
        self.column(3270, 4200, 3975)
        self.column(2825, 3050, 3975)
        self.column(3970, 4200, 3025)
        self.column(2825, 3750, 3025)
        self.row(3025, 4000, 2825)

        self.column(3100, 4000, 3325)
        self.column(3100, 4000, 3675)

        self.column(2125, 2825, 2620.5)

        self.row(2300, 3000, 3050)

        self.column(1900, 2100, 3500)
        self.column(1400, 1601, 3500)


        self.physics_engine2 = arcade.PhysicsEngineSimple(self.enemy_list[0], self.wall_list)
        self.physics_engine3 = arcade.PhysicsEngineSimple(self.enemy_list[1], self.wall_list)
        self.physics_engine4 = arcade.PhysicsEngineSimple(self.enemy_list[2], self.wall_list)
        self.physics_engine5 = arcade.PhysicsEngineSimple(self.enemy_list[3], self.wall_list)
        self.physics_engine6 = arcade.PhysicsEngineSimple(self.enemy_list[4], self.wall_list)
        self.physics_engine7 = arcade.PhysicsEngineSimple(self.enemy_list[5], self.wall_list)
        self.physics_engine8 = arcade.PhysicsEngineSimple(self.enemy_list[6], self.wall_list)
        self.physics_engine9 = arcade.PhysicsEngineSimple(self.enemy_list[7], self.wall_list)
        self.physics_engine10 = arcade.PhysicsEngineSimple(self.enemy_list[8], self.wall_list)
        self.physics_engine11 = arcade.PhysicsEngineSimple(self.enemy_list[9], self.wall_list)
        self.physics_engine13 = arcade.PhysicsEngineSimple(self.enemy_list[10], self.wall_list)
        self.physics_engine12 = arcade.PhysicsEngineSimple(self.enemy_list[11], self.wall_list)
        self.physics_engine14 = arcade.PhysicsEngineSimple(self.enemy_list[12], self.wall_list)

        self.physics_engine_p1 = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        self.physics_engine_p2 = arcade.PhysicsEngineSimple(self.player_sprite, self.door_list)

    def floor(self):
        for x in range(-500, 3001, 1000):
            for y in range(350, 351, 700):
                arcade.draw_ellipse_filled(x, y,1000, 700, (200,173,93))
                arcade.draw_ellipse_filled(x, y, 700, 450, (190,163,83))

        arcade.draw_lrtb_rectangle_filled(0, 5200, 4550, 1300, (57,24,6))
        for x in range(-350, 5200, 350):
            for y in range(1300, 4550, 400):
                arcade.draw_lrtb_rectangle_filled(x, x + 340, y + 200, y + 20, (120,94,48))
                arcade.draw_lrtb_rectangle_filled(x + 165, x + 505, y + 400, y + 220,(120,94,48))

    def row(self, start_x, end_x, y):
        self.walls = ["tile_0004.png", "tile_0003.png", "tile_0001.png"]
        for x in range(start_x, end_x, 50):
            if y > 1000:
                if x == 0:
                    block = 1
                if x % 7 == 0:
                    block = 0
                else:
                    block = 1

                wall = arcade.Sprite(self.walls[block], 3.16)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)
            elif y <= 1000:
                wall = arcade.Sprite(self.walls[2], 3.16)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

    def column(self, start_y, end_y, x):
        self.walls = ["tile_0004.png", "tile_0003.png", "tile_0001.png"]
        for y in range(start_y, end_y, 50):
            if start_y > 1000:
                if y == 0:
                    block = 1
                elif y % 7 == 0:
                    block = 0
                    wall = arcade.Sprite(self.walls[block], 3.16)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)
                else:
                    block = 1
                    wall = arcade.Sprite(self.walls[block], 3.16)
                    wall.center_x = x
                    wall.center_y = y
                    self.wall_list.append(wall)

            elif start_y < 1000:
                wall = arcade.Sprite(self.walls[2], 3.16)
                wall.center_x = x
                wall.center_y = y
                self.wall_list.append(wall)

    def room(self, center_x, center_y, left_door = False, right_door = False, up_door = False, down_door = False):
        if left_door == True:
            self.column(center_y+120, center_y+326, center_x-475)
            self.column(center_y-325, center_y-101, center_x-475)
        else:
            self.column(center_y -300, center_y + 301, center_x - 475)

        if right_door == True:
            self.column(center_y + 120, center_y + 326, center_x + 475)
            self.column(center_y - 325, center_y - 101, center_x + 475)
        else:
            self.column(center_y - 325, center_y + 326, center_x + 475)

        if down_door == True:
            self.row(center_x + 120, center_x + 476, center_y - 325)
            self.row(center_x - 475, center_x - 101, center_y - 325)
        else:
            self.row(center_x - 476, center_x + 476, center_y - 325)

        if up_door == True:
            self.row(center_x + 120, center_x + 476, center_y + 325)
            self.row(center_x - 475, center_x - 101, center_y + 325)
        else:
            self.row(center_x - 475, center_x + 476, center_y + 325)

    def on_draw(self):
        self.clear()

        self.camera_sprites.use()
        arcade.set_background_color((70,150,70))
        self.floor()
        arcade.draw_text("Press W to swing your sword", 2310, 200, arcade.color.BLACK_LEATHER_JACKET, 20)
        arcade.draw_text("Use the arrow keys to move", 310, 500, arcade.color.BLACK_LEATHER_JACKET, 20)
        arcade.draw_text("Collect treasure to increase your score", 1270, 500, arcade.color.BLACK_LEATHER_JACKET, 20)
        arcade.draw_text("you've found a staff!", 1300, 4046, arcade.color.RED, 20)
        arcade.draw_text("press e to see what it does", 1300, 3710, arcade.color.RED, 20)
        if self.door == True:
            arcade.draw_text("you may need a key...", 4395, 2963, arcade.color.WHITE, 20)
        arcade.draw_text("welcome to The Maze", 196, 3358, arcade.color.WHITE, 20)
        arcade.draw_text("your goal is to retrieve the diamond at the end", 196, 3278, arcade.color.WHITE, 20)
        arcade.draw_text("good luck!", 196, 3198, arcade.color.WHITE, 20)


        for y in range(0, 151, 50):
            self.false_wall = arcade.Sprite("tile_0003.png", 3)
            self.false_wall.center_x = 2015
            self.false_wall.center_y = 3775 + y
            self.false_wall.draw()


        self.wall_list.draw()
        self.player_list.draw()
        self.chest_list.draw()
        self.coin_list.draw()
        self.enemy_list.draw()
        self.weapon_list.draw()
        self.key_list.draw()
        self.staff_list.draw()
        self.door_list.draw()
        self.boss_list.draw()

        self.camera_gui.use()
        if self.hp >= 1:
            self.heart_sprite1.draw()
        if self.hp >= 2:
            self.heart_sprite2.draw()
        if self.hp >= 3:
            self.heart_sprite3.draw()

        arcade.draw_text("Score: " + str(self.score), 10, 20, arcade.color.WHITE, 14)
        if self.hp <= 0:
            arcade.draw_rectangle_filled(500, 350, 1000, 700, (0,0,0))
            arcade.draw_text(("GAME"), 140, 450, arcade.color.CHINESE_RED, 150)
            arcade.draw_text(("OVER"), 190, 300, arcade.color.CHINESE_RED, 150)
            arcade.draw_text("gold collected: " + str(self.gold_collected), 30, 50, arcade.color.GOLD, 35)
            arcade.draw_text("enemys defeated: " + str(self.enemys_defeated), 30, 100, arcade.color.GRAY, 35)
            arcade.draw_text("Score: " + str(self.score), 500, 70, arcade.color.WHITE, 40)
        if self.win == True:
            arcade.draw_text(("you win!"), 140, 450, arcade.color.GOLD, 150)
            arcade.draw_text("gold collected: " + str(self.gold_collected), 30, 50, arcade.color.GOLD, 35)
            arcade.draw_text("enemys defeated: " + str(self.enemys_defeated), 30, 100, arcade.color.GRAY, 35)
            arcade.draw_text("Score: " + str(self.score), 500, 70, arcade.color.WHITE, 40)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
            if self.sword_timer == self.sword_timer < 0:
                self.pointing = UP
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
            if self.sword_timer == self.sword_timer < 0:
                self.pointing = DOWN
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
            if self.sword_timer == self.sword_timer < 0:
                self.pointing = LEFT
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
            if self.sword_timer == self.sword_timer < 0:
                self.pointing = RIGHT

        if self.sword_timer < 0:
            if key == arcade.key.W:
                self.sword_check = True
                self.sword_timer = 20
                if self.pointing == -3 or self.pointing == 4:
                    self.sword_sprite.center_x = self.player_sprite.center_x + (self.pointing / abs(self.pointing)) * 20
                    self.sword_sprite.center_y = self.player_sprite.center_y - 10


                if self.pointing == 1 or self.pointing == -2:
                    self.sword_sprite.center_y = self.player_sprite.center_y - 10 + (self.pointing / abs(self.pointing)) * 20
                    self.sword_sprite.center_x = self.player_sprite.center_x

        if self.wand == True:
            if key == arcade.key.E:
                self.bow_timer = 0
                self.arrow_start_x = self.player_sprite.center_x
                self.arrow_start_y = self.player_sprite.center_y
                self.pointing_at_shot = self.pointing

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def enemy_movement(self):
        for x in range(len(self.enemy_list)):

            if ((self.enemy_list[x].center_x - int(self.camera_sprites.position[0])) > 0 and
                (self.enemy_list[x].center_x - int(self.camera_sprites.position[0])) < 1000) and ((self.enemy_list[x].center_y - int(self.camera_sprites.position[1])) > 0 and
                (self.enemy_list[x].center_y - int(self.camera_sprites.position[1])) < 700):

                self.track_x = self.enemy_list[x].center_x - self.player_sprite.center_x
                self.track_y = self.enemy_list[x].center_y - self.player_sprite.center_y

                if self.track_x > 0:
                    self.enemy_list[x].center_x -= 1.5
                else:
                    self.enemy_list[x].center_x += 1.5

                if self.track_y > 0:
                    self.enemy_list[x].center_y -= 1.5
                else:
                    self.enemy_list[x].center_y += 1.5
                self.track_list_x.append(self.track_x)
                self.track_list_y.append(self.track_y)
        if self.boss_hp > 0:
            if ((self.boss_list[0].center_x - int(self.camera_sprites.position[0])) > 0 and
                (self.boss_list[0].center_x - int(self.camera_sprites.position[0])) < 1000) and (
                    (self.boss_list[0].center_y - int(self.camera_sprites.position[1])) > 0 and
                    (self.boss_list[0].center_y - int(self.camera_sprites.position[1])) < 700):

                self.track_x = self.boss_list[0].center_x - self.player_sprite.center_x
                self.track_y = self.boss_list[0].center_y - self.player_sprite.center_y

                if self.track_x > 0:
                    self.boss_list[0].center_x -= 1.5
                else:
                    self.boss_list[0].center_x += 1.5

                if self.track_y > 0:
                    self.boss_list[0].center_y -= 1.5
                else:
                    self.boss_list[0].center_y += 1.5
                self.track_list_x.append(self.track_x)
                self.track_list_y.append(self.track_y)

    def sword_movement(self):
        if self.sword_timer > -1:
            self.sword_timer -= 1
        elif self.sword_timer < 0:
            self.sword_sprite.center_y = -100
            self.sword_sprite.center_x = 0
            self.sword_sprite.angle = 0
            self.sword_check = False

        if self.pointing == 1:
            self.sword_sprite.angle = -80 + self.sword_timer * (self.pointing / abs(self.pointing)) * 8
        elif self.pointing == -2:
            self.sword_sprite.angle = 100 - self.sword_timer * (self.pointing / abs(self.pointing)) * 8
        elif self.pointing == -3:
            self.sword_sprite.angle = 10 - self.sword_timer * (self.pointing / abs(self.pointing)) * 8
        elif self.pointing == 4:
            self.sword_sprite.angle = 180 + self.sword_timer * (self.pointing / abs(self.pointing)) * 8

    def arrow_movement(self):
        self.bow_timer += 8
        if self.pointing_at_shot == UP:
            self.arrow_sprite.center_x = self.arrow_start_x
            self.arrow_sprite.center_y = self.arrow_start_y + self.bow_timer
        if self.pointing_at_shot == DOWN:
            self.arrow_sprite.center_x = self.arrow_start_x
            self.arrow_sprite.center_y = self.arrow_start_y - self.bow_timer
        if self.pointing_at_shot == RIGHT:
            self.arrow_sprite.center_y = self.arrow_start_y
            self.arrow_sprite.center_x = self.arrow_start_x + self.bow_timer
        if self.pointing_at_shot == LEFT:
            self.arrow_sprite.center_y = self.arrow_start_y
            self.arrow_sprite.center_x = self.arrow_start_x - self.bow_timer

    def on_update(self, delta_time):
        self.win_sound =  arcade.load_sound("win.wav")
        self.good_sound = arcade.load_sound("coin.wav")
        self.hit_sound = arcade.load_sound("hit.wav")
        self.key_sound = arcade.load_sound("door.wav")

        if self.hp <= 0:
            self.player_sprite.center_x = -10000
        if self.door == False:
         for x in range(len(self.door_list)):
             self.door_list[x].center_x = 1000000

        self.sword_movement()
        self.arrow_movement()

        if (((int(self.camera_sprites.position[0]) % 1000 <= 9 or int(self.camera_sprites.position[0]) % 1000 >= 991)
                and (int(self.camera_sprites.position[1]) % 700 <= 9 or int(self.camera_sprites.position[1]) % 700 >= 691)) and
                self.hp > 0):
            self.enemy_movement()
            self.physics_engine2.update()
            self.physics_engine3.update()
            self.physics_engine4.update()
            self.physics_engine5.update()
            self.physics_engine6.update()
            self.physics_engine7.update()
            self.physics_engine8.update()
            self.physics_engine9.update()
            self.physics_engine10.update()
            self.physics_engine11.update()
            self.physics_engine12.update()
            self.physics_engine13.update()
            self.physics_engine14.update()

        if (((int(self.camera_sprites.position[0]) % 1000 <= 9 or int(self.camera_sprites.position[0]) % 1000 >= 991)
             and (int(self.camera_sprites.position[1]) % 700 <= 9 or int(
                    self.camera_sprites.position[1]) % 700 >= 691)) and
                self.hp > 0) and self.sword_check == False and self.win == False:
            self.physics_engine_p1.update()
            self.physics_engine_p2.update()

        self.weapon_list.update()
        self.scroll_to_player()

        treasure_collected = arcade.check_for_collision_with_list(self.player_sprite, self.chest_list)
        for chest in treasure_collected:
            chest.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.score += 10
            self.win = True
            arcade.play_sound(self.win_sound)

        coins_collected = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_collected:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.good_sound)
            self.gold_collected += 1
            self.score += 5
            if self.player_sprite.center_x > 4400 and self.player_sprite.center_x < 4600:
                self.enemy_list[-2].center_x = 4100
                self.enemy_list[-2].center_y = 3180

                self.enemy_list[-1].center_x = 4500
                self.enemy_list[-1].center_y = 2930

        staff_collected = arcade.check_for_collision_with_list(self.player_sprite, self.staff_list)
        for staff in staff_collected:
            self.wand = True
            staff.remove_from_sprite_lists()

        if self.hit_timer > 0:
            self.hit_timer -= 1
        if self.hit_timer <= 0:
            hit_count =  arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
            for hit in hit_count:
                self.hp -= 1
                if hit.position[0] > (10 + self.player_sprite.center_x):
                    self.player_sprite.center_x -= 30
                elif hit.position[0] < (self.player_sprite.center_x - 10):
                        self.player_sprite.center_x += 30
                else:
                    pass

                if hit.position[1] > (10 + self.player_sprite.center_y):
                    self.player_sprite.center_y -= 30
                elif hit.position[1] < (self.player_sprite.center_y - 10):
                    self.player_sprite.center_y += 30
                else:
                    pass

                self.hit_timer = 60
                arcade.play_sound(self.hit_sound)

        damage_dealt  = arcade.check_for_collision_with_list(self.sword_sprite, self.enemy_list)
        for enemy in damage_dealt:
            self.enemys_defeated += 1
            self.score += 1
            enemy.remove_from_sprite_lists()
            arcade.play_sound(self.hit_sound)

        damage_dealt = arcade.check_for_collision_with_list(self.arrow_sprite, self.enemy_list)
        for enemy in damage_dealt:
            self.enemys_defeated += 1
            self.score += 1
            enemy.remove_from_sprite_lists()
            arcade.play_sound(self.hit_sound)

        wall_hit = arcade.check_for_collision_with_list(self.arrow_sprite, self.wall_list)
        for arrow in wall_hit:
            self.bow_timer = -1000000

        if self.player_sprite.center_x >= 2983 and self.player_sprite.center_x <= 3000 and self.player_sprite.center_y > 100 and self.player_sprite.center_y < 600:
            self.player_sprite.center_x = 500
            self.player_sprite.center_y = 3150
            self.camera_sprites.move_to(Vec2(500, 3150), 1.2)
            self.score = 0
            self.enemys_defeated = 0
            self.gold_collected = 0
            self.hp = 3

        keys_collected = arcade.check_for_collision_with_list(self.player_sprite, self.key_list)
        for key in keys_collected:
            self.door = False
            key.remove_from_sprite_lists()
            arcade.play_sound(self.key_sound)

        if self.boss_timer >= -2:
            self.boss_timer -= 1

        if self.boss_timer <= 0:
            boss_damage_dealt = arcade.check_for_collision_with_list(self.sword_sprite, self.boss_list)
            for boss in boss_damage_dealt:
                if self.boss_timer <= 0:
                    arcade.play_sound(self.hit_sound)
                    self.boss_hp -= 1
                    self.boss_timer = 30
                    if self.boss_hp <= 0:
                        self.enemys_defeated += 1
                        self.score += 15
                        boss.remove_from_sprite_lists()


        if self.hit_timer <= 0:
            hit_count =  arcade.check_for_collision_with_list(self.player_sprite, self.boss_list)
            for hit in hit_count:
                self.hp -= 1
                if hit.position[0] > (10 + self.player_sprite.center_x):
                    self.player_sprite.center_x -= 30
                elif hit.position[0] < (self.player_sprite.center_x - 10):
                        self.player_sprite.center_x += 30
                else:
                    pass

                if hit.position[1] > (10 + self.player_sprite.center_y):
                    self.player_sprite.center_y -= 30
                elif hit.position[1] < (self.player_sprite.center_y - 10):
                    self.player_sprite.center_y += 30
                else:
                    pass
                self.hit_timer = 60
                arcade.play_sound(self.hit_sound)

    def scroll_to_player(self):
        if self.player_sprite.center_x < self.cam_x:
            self.cam_x -= 1000

        if self.player_sprite.center_x > self.cam_x + 1000:
            self.cam_x += 1000

        if self.player_sprite.center_y < self.cam_y:
            self.cam_y -= 700

        if self.player_sprite.center_y > self.cam_y + 700:
            self.cam_y += 700

        position = Vec2(self.cam_x, self.cam_y)
        self.camera_sprites.move_to(position, 0.125)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()