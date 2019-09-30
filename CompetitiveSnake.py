import arcade


WIDTH = 800
HEIGHT = 600

# TODO: create general button class

class Button:
    def __init__(x, y, w, h, color, filled, buttontype):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.filled = filled
        self.type = buttontype
    
    def draw_button(self):
        if self.filled:
            if self.buttontype == "standard":
                arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.color)
            elif self.buttontype == "ltrb":
                arcade.draw_lrtb_rectangle_filled(self.x, self.y, self.w, self.h, self.color)
            elif self.buttontype == "xywh":
                arcade.draw_xywh_rectangle_filled(self.x, self.y, self.w, self.h, self.color)
        if not self.filled:
            if self.buttontype == "standard":
                arcade.draw_rectangle_outline(self.x, self.y, self.w, self.h, self.color)
            elif self.buttontype == "ltrb":
                arcade.draw_lrtb_rectangle_outline(self.x, self.y, self.w, self.h, self.color)
            elif self.buttontype == "xywh":
                arcade.draw_xywh_rectangle_outline(self.x, self.y, self.w, self.h, self.color)


# Start screen variables
on_start_screen = True
start_key_pressed = False
start_key_rgb = arcade.color.GREEN
start_rgb_rgb_target = arcade.color.GO_GREEN

on_play_screen = False

def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    if on_start_screen:
        draw_start_screen()
    elif on_play_screen:
        draw_grid()


def draw_start_screen():
    global start_key_pressed
    if not start_key_pressed:
        arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, 300, 100, arcade.color.GREEN)
    elif start_key_pressed:
        arcade.draw_rectangle_filled(WIDTH/2, HEIGHT/2, 300, 100, arcade.color.GO_GREEN)


def draw_grid():
    arcade.draw_xywh_rectangle_outline(1, 1, WIDTH-1, HEIGHT-2, arcade.color.RED)
    for i in range(int(WIDTH/20)):
        arcade.draw_line(i*20, 0, i*20, HEIGHT, arcade.color.BLACK)
    for i in range(int(HEIGHT/20)):
        arcade.draw_line(0, i*20, WIDTH, i*20, arcade.color.BLACK)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global start_key_pressed
    if WIDTH/2 - 150 <= x <= WIDTH/2 + 150:
        if HEIGHT/2 - 50 <= y <= HEIGHT/2 + 50:
            start_key_pressed = True


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
