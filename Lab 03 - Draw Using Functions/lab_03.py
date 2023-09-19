import arcade
#moon
def the_moon(center_x, center_y, background_color):
    arcade.draw_circle_filled(center_x, center_y, 50, (180, 180, 180))
    arcade.draw_circle_filled(center_x - 25, center_y, 50, background_color)

#draws tree from bottom left
def tree(left, bottom):
    arcade.draw_lrtb_rectangle_filled(left, left + 30, bottom+20, bottom, arcade.color.KENYAN_COPPER)
    arcade.draw_triangle_filled(left - 26, bottom + 19, left + 15, bottom + 151, left + 51, bottom + 19, arcade.color.BLACK)
    arcade.draw_triangle_filled(left - 25,bottom + 20, left + 15, bottom + 150, left + 50, bottom + 20, arcade.color.DARK_GREEN)
# Star
def star(center_x, center_y):
    arcade.draw_circle_filled(center_x , center_y, 1, (240, 240 ,240))

# Background
arcade.open_window(800, 600, "Lab_3")
arcade.set_background_color(arcade.color.DARK_MIDNIGHT_BLUE)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 800, 400, 0, arcade.color.KOMBU_GREEN)

# Lake
arcade.draw_ellipse_filled(600, 325, 750, 250, (183, 111, 85))
arcade.draw_ellipse_filled(600, 325, 700, 200, (0, 31, 80))
the_moon(700, 500-175, (0, 31, 80))
star(532, 300)
star(512, 381)
star(451, 338)
star(600, 350)
star(615, 250)
star(325, 288)
star(278, 400 - 65)
star(351, 400 - 110)

# Sky
arcade.draw_lrtb_rectangle_filled(0, 800, 600, 400, arcade.color.DARK_MIDNIGHT_BLUE)
the_moon(700, 500, arcade.color.DARK_MIDNIGHT_BLUE)
star(278, 465)
star(532,500)
star(325, 512)
star(512, 419)
star(215,540)
star(351, 510)
star(451, 468)
star(145, 590)
star(95, 450)
star(60, 500)
star(600, 450)
star(615, 550)

# trees, a lot of trees
for i in range(1, 6):
    tree(70, 365 - (i * 74))
    tree(12, 360 - (i *76))
    tree(130, 345 - (i * 74))

arcade.finish_render()
arcade.run()