import arcade


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
arcade.draw_lrtb_rectangle_filled(220, 240, 140, 120, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(300, 320, 140, 120, arcade.color.YELLOW)
arcade.draw_triangle_filled(175, 180, 275, 250, 375, 180, arcade.color.RADICAL_RED)
arcade.draw_lrtb_rectangle_filled(300, 320, 140, 120, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(260, 280, 140, 100, arcade.color.RADICAL_RED)

arcade.finish_render()
arcade.run()