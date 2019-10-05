import arcade


WIDTH = 800
HEIGHT = 600

# TODO: add to general button class

class Button:
    def empty():
        pass
    def __init__(self, x, y, w, h, color, filled, buttontype):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.filled = filled
        self.buttontype = buttontype
        self.clickevent = Button.empty
        self.enablebutton = True
        self.displaytext = True

    def onClick(self, func):
      	self.clickevent = func
    
    def text_arguments(self, *args, **kwargs):
        self._text_args = args
        self._text_kwargs = kwargs

    def check_press(self, x, y):
        if self.enablebutton:
            if self.buttontype == "standard":
                if self.x - self.w/2 <= x <= self.x + self.w/2 \
                    and self.y - self.h/2 <= y <= self.y + self.h/2:
                    return True, self.clickevent()
            elif self.buttontype == "xywh":
                if self.x < x < (self.x + self.w) \
                    and self.y < y < (self.y + self.h):
                        return True, self.clickevent()
            elif self.buttontype == "ltrb":
                if self.x < x < self.w \
                    and self.y > y > self.h:
                    return True, self.clickevent()
        return False,
    
    def draw(self):
        if self.enablebutton:
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
            if self.displaytext:
                arcade.draw_text(*self._text_args, **self._text_kwargs)


# Start screen setup
on_start_screen = True
start_key_pressed = False
start_key_rgb = (255, 255, 255)
start_button = Button(WIDTH/2, HEIGHT/2, 300, 100, arcade.color.GREEN, True, "standard")
start_button.text_arguments("PLAY", WIDTH/2 - 60, HEIGHT/2 - 25, arcade.color.WHITE, font_size=50)


# Play screen setup
on_play_screen = False

def on_update(delta_time):
    pass


def on_draw():
    global on_start_screen, on_play_screen, start_key_rgb, start_key_pressed
    arcade.start_render()
    if on_start_screen:
        draw_start_screen()
        if start_key_pressed:
            if start_key_rgb[0] > 0:
                start_key_rgb = (start_key_rgb[0] - 3, start_key_rgb[1] - 3, start_key_rgb[2] - 3)
                arcade.set_background_color(start_key_rgb)
            if start_key_rgb[0] == 0:
                on_start_screen = False
                on_play_screen = True
            print(start_key_rgb)
    elif on_play_screen:
        background = arcade.load_texture("assets/grid_background.png")
        arcade.draw_texture_rectangle(WIDTH/2, HEIGHT/2, 800, 600, background)


def draw_start_screen():
    start_button.draw()


def draw_start_screen_animation():
    global start_key_rgb, on_start_screen, on_play_screen
    arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT, start_key_rgb)

    if on_start_screen:
        arcade.set_background_color(arcade.color.WHITE)
    elif on_play_screen:
        arcade.set_background_color(arcade.color.BLACK)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global start_key_pressed, start_button
    if start_button.check_press(x, y)[0]:
        start_button.enablebutton = False
        start_button.displaytext = False
        start_key_pressed = True


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLUE)
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