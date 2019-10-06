import logging
import os
import random
import arcade

logging.basicConfig(level=logging.DEBUG)

UPDATE_HERTZ = 4

SNAKE_1_CONTROLS = {arcade.key.W: 0, arcade.key.D: 1, arcade.key.S: 2, arcade.key.A: 3}
SNAKE_1_COLOR = arcade.color.GREEN
SNAKE_2_CONTROLS = {arcade.key.UP: 0, arcade.key.RIGHT: 1, arcade.key.DOWN: 2, arcade.key.LEFT: 3}
SNAKE_2_COLOR = arcade.color.YELLOW

SCREEN_WIDTH = WIDTH = 800
SCREEN_HEIGHT = HEIGHT = 600
SCREEN_TITLE = f"Competitive Snake (from {__file__})"


class Button:

    def __init__(self, x, y, w, h, color, filled, buttontype):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.filled = filled
        self.buttontype = buttontype
        self.clickevent = lambda: None
        self.enablebutton = True
        self.displaytext = True

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
            "color_code": 255,
            "snake_direction_1": 0,
            "snake_direction_2": 0,
            "win_state": 0
        }
        self.background = None
        self.snake1 = [(1,1), (1,2), (1,3), (1,4), (1,5)]
        self.snake2 = [(38,1), (38,2), (38,3), (38,4), (38, 5)]
        self.snake1_len = 5
        self.snake2_len = 5
        arcade.set_background_color(arcade.color.WHITE)
        self.start_button = Button(WIDTH/2, HEIGHT/2, 300, 100, arcade.color.GREEN, True, "standard")
        self.start_button.text_arguments("PLAY", WIDTH/2 - 60, HEIGHT/2 - 25, arcade.color.WHITE, font_size=50)

    def _draw_tile(self, tile, color):
        arcade.draw_xywh_rectangle_filled(20*tile[0] + 1, 20*tile[1] + 1, 19, 19, color)
    
    def draw_snake(self, snake, color):
        for i in snake:
            self._draw_tile(i, color)

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
            self.draw_snake(self.snake1, SNAKE_1_COLOR)
            self.draw_snake(self.snake2, SNAKE_2_COLOR)
        elif self.flags["win_state"] == 1:
            print("Win state 1, exiting...")
            arcade.close_window()
        elif self.flags["win_state"] == 2:
            print("Win state 2, exiting...")
            arcade.close_window()


    def draw_start_screen(self):
        self.start_button.draw()


    def on_key_press(self, key, modifiers):
        if self.flags["on_play_screen"]:
            try:
                new_direction = SNAKE_1_CONTROLS[key]
                if abs(new_direction - self.flags["snake_direction_1"]) != 2:
                    self.flags["snake_direction_1"] = new_direction
            except KeyError:
                print("Key error 1")
                pass
            try:
                new_direction2 = SNAKE_2_CONTROLS[key]
                if abs(new_direction2 - self.flags["snake_direction_2"]) != 2:
                    self.flags["snake_direction_2"] = new_direction2
            except KeyError:
                print("Key error 2")
                pass


    def on_key_release(self, key, modifiers):
        pass


    def on_mouse_press(self, x, y, button, modifiers):
        if self.start_button.check_press(x, y)[0]:
            self.start_button.enablebutton = False
            self.start_button.displaytext = False
            self.flags["start_key_pressed"] = True


    def update(self, delta_time):
        if self.flags["on_play_screen"]:
            *snake_body, snake_head = self.snake1
            print(snake_head)
            if snake_head[1] < 0 or snake_head[1] > 28 or \
                snake_head[0] < 0 or snake_head[0] > 39 or \
                snake_head in snake_body or \
                snake_head in self.snake2:
                self.flags["on_play_screen"] = False
                self.flags["win_state"] = 2
                

            self.set_update_rate(1/UPDATE_HERTZ)
            if self.flags["snake_direction_1"] == 0:
                self.snake1.append((snake_head[0], snake_head[1] + 1))
            elif self.flags["snake_direction_1"] == 1:
                self.snake1.append((snake_head[0] + 1, snake_head[1]))
            elif self.flags["snake_direction_1"] == 2:
                self.snake1.append((snake_head[0], snake_head[1] - 1))
            elif self.flags["snake_direction_1"] == 3:
                self.snake1.append((snake_head[0] - 1, snake_head[1]))
            if len(self.snake1) > self.snake1_len:
                del self.snake1[0]


            *snake_body, snake_head = self.snake2
            print(snake_head)
            if snake_head[1] < 0 or snake_head[1] > 28 or \
                snake_head[0] < 0 or snake_head[0] > 39 or \
                snake_head in snake_body or \
                snake_head in self.snake1:
                self.flags["on_play_screen"] = False
                self.flags["win_state"] = 1
                

            self.set_update_rate(1/UPDATE_HERTZ)
            if self.flags["snake_direction_2"] == 0:
                self.snake2.append((snake_head[0], snake_head[1] + 1))
            elif self.flags["snake_direction_2"] == 1:
                self.snake2.append((snake_head[0] + 1, snake_head[1]))
            elif self.flags["snake_direction_2"] == 2:
                self.snake2.append((snake_head[0], snake_head[1] - 1))
            elif self.flags["snake_direction_2"] == 3:
                self.snake2.append((snake_head[0] - 1, snake_head[1]))
            if len(self.snake2) > self.snake2_len:
                del self.snake2[0]


    def setup(self):
        self.background = arcade.load_texture("assets/grid_background.png")
        # arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
        logging.debug("Done setup()")

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    try:
        arcade.run()
    except AttributeError:
        print("Exiting with no errors.")  # If you see this text, it exited with a lot of errors and I don't know why.


if __name__ == "__main__":
    main()
