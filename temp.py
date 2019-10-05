import random
import arcade
import os
import logging

logging.basicConfig(level=logging.DEBUG)

SPRITE_SCALING = 0.5

SCREEN_WIDTH = WIDTH = 800
SCREEN_HEIGHT = HEIGHT = 600
SCREEN_TITLE = f"Competitive Snake (from {__file__})"


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

class MyGame(arcade.Window):

    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(width, height, title)
        self.flags = {
            "on_start_screen": True,
            "on_play_screen":  False,
            "start_key_pressed": False,
            "color_code": 255
        }
        self.background = None

        arcade.set_background_color(arcade.color.WHITE)
        self.start_button = Button(WIDTH/2, HEIGHT/2, 300, 100, arcade.color.GREEN, True, "standard")
        self.start_button.text_arguments("PLAY", WIDTH/2 - 60, HEIGHT/2 - 25, arcade.color.WHITE, font_size=50)

    def on_draw(self):
        arcade.start_render()
        if self.flags["on_start_screen"]:
            self.draw_start_screen()
            if self.flags["start_key_pressed"]:
                if self.flags["color_code"] > 0:
                    arcade.set_background_color((self.flags["color_code"], self.flags["color_code"], self.flags["color_code"]))
                    self.flags["color_code"] -= 3
                else:
                    self.flags["on_start_screen"] = False
                    self.flags["on_play_screen"] = True
        elif self.flags["on_play_screen"]:
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                         SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # Render the text

    def draw_start_screen(self):
        self.start_button.draw()


    def draw_start_screen_animation(self):
        arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT, start_key_rgb)

        if self.flags["on_start_screen"]:
            arcade.set_background_color(arcade.color.WHITE)
        elif self.flags["on_play_screen"]:
            arcade.set_background_color(arcade.color.BLACK)


    def on_key_press(self, key, modifiers):
        pass


    def on_key_release(self, key, modifiers):
        pass


    def on_mouse_press(self, x, y, button, modifiers):
        if self.start_button.check_press(x, y)[0]:
            self.start_button.enablebutton = False
            self.start_button.displaytext = False
            self.flags["start_key_pressed"] = True

    def update(self, delta_time):
        pass

    def setup(self):
        self.background = arcade.load_texture("assets/grid_background.png")
        # arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
        logging.debug("Done setup()")

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()