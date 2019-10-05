"""
Sprite Collect Coins with Background

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_collect_coins_background
"""
import random
import arcade
import os

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Collect Coins with Background Example"


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
        self.flags = {}


    def on_draw(self):
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
            draw_grid()
        # Render the text

    def draw_start_screen():
        start_button.draw()


    def draw_start_screen_animation():
        global start_key_rgb, on_start_screen, on_play_screen
        arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT, start_key_rgb)

        if on_start_screen:
            arcade.set_background_color(arcade.color.WHITE)
        elif on_play_screen:
            arcade.set_background_color(arcade.color.BLACK)


    def draw_grid():
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_xywh_rectangle_outline(1, 0, WIDTH-1, HEIGHT-1, arcade.color.RED)
        for i in range(1, int(WIDTH/20)):
            arcade.draw_line(i*20, 0, i*20, HEIGHT, arcade.color.WHITE)
        for i in range(1, int(HEIGHT/20)):
            arcade.draw_line(1, i*20, WIDTH, i*20, arcade.color.WHITE)


    def on_key_press(key, modifiers):
        pass


    def on_key_release(key, modifiers):
        pass


    def on_mouse_press(x, y, button, modifiers):
        if start_button.check_press(x, y)[0]:
            start_button.enablebutton = False
            start_button.displaytext = False
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

def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()