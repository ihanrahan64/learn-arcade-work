import arcade


def tree(left, bottom):
    arcade.draw_lrtb_rectangle_filled(left, left + 30, bottom+20, bottom, arcade.color.BROWN)
    arcade.draw_triangle_filled(left - 26, bottom + 19, left + 15, bottom + 151, left + 51, bottom + 19, arcade.color.BLACK)
    arcade.draw_triangle_filled(left - 25,bottom + 20, left + 15, bottom + 150, left + 50, bottom + 20, arcade.color.DARK_GREEN)

# Starting window
arcade.open_window(600, 400, "Lab_2")
arcade.set_background_color(arcade.color.BLUE_YONDER)
arcade.start_render()

# Ground
arcade.draw_lrtb_rectangle_filled(0, 600, 280, 0, arcade.color.BANGLADESH_GREEN)

# River
arcade.draw_circle_filled(1200, -100,  800, arcade.color.BLUE_SAPPHIRE)
arcade.draw_circle_filled(1200, -100,  770, arcade.color.BANGLADESH_GREEN)

# Sky
arcade.draw_lrtb_rectangle_filled(0, 600, 400, 280, arcade.color.BLUE_YONDER)
arcade.draw_circle_filled(500, 350, 35, arcade.color.GOLD)

# House
arcade.draw_lrtb_rectangle_filled(200, 350, 190, 100, arcade.color.SKY_BLUE)

# Windows
arcade.draw_lrtb_rectangle_filled(220, 240, 140, 120, arcade.color.WHITE_SMOKE)
arcade.draw_lrtb_rectangle_filled(223, 237, 137, 123, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(300, 320, 140, 120, arcade.color.WHITE_SMOKE)
arcade.draw_lrtb_rectangle_filled(303, 317, 137, 123, arcade.color.YELLOW)

# Roof
arcade.draw_triangle_filled(175, 180, 275, 250, 375, 180, (255, 53, 94))

# Door
arcade.draw_lrtb_rectangle_filled(260, 280, 140, 100, arcade.color.RADICAL_RED)

# Trees
tree(20, 50)
tree(80, 120)

arcade.finish_render()
arcade.run()