import arcade


WIDTH = 800
HEIGHT = 600


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    draw_grid()


def draw_grid():
    arcade.draw_xywh_rectangle_outline(1, 1, WIDTH-1, HEIGHT-2, color=arcade.color.RED)
    for i in range(int(WIDTH/20)):
        arcade.draw_line(i*20, 0, i*20, HEIGHT, color=arcade.color.BLACK)
    for i in range(int(HEIGHT/20)):
        arcade.draw_line(0, i*20, WIDTH, i*20, color=arcade.color.BLACK)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
