import arcade


WIDTH = 800
HEIGHT = 600

# TODO: add to general button class

buttons = []

def get_button_index_by_id(buttonid):
    button_index = -1
    for i in range(len(buttons)):
        if buttons[i].buttonid == buttonid:
            button_index = i
            break
    if button_index == -1:
        print(f"ERROR: no button with id {buttonid} found")
    return button_index

class Button:
    def __init__(self, buttonid, x, y, w, h, color, filled, buttontype):
        self.buttonid = buttonid
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.filled = filled
        self.buttontype = buttontype
    
    def create(self):
        buttons.append(self)
    
    def draw(buttonid):
        button_index = get_button_index_by_id(buttonid)
        if button_index != -1:
            if buttons[button_index].filled:
                if buttons[button_index].buttontype == "standard":
                    arcade.draw_rectangle_filled(buttons[button_index].x, buttons[button_index].y, buttons[button_index].w, buttons[button_index].h, buttons[button_index].color)
                elif buttons[button_index].buttontype == "ltrb":
                    arcade.draw_lrtb_rectangle_filled(buttons[button_index].x, buttons[button_index].y, buttons[button_index].w, buttons[button_index].h, buttons[button_index].color)
                elif buttons[button_index].buttontype == "xywh":
                    arcade.draw_xywh_rectangle_filled(buttons[button_index].x, buttons[button_index].y, buttons[button_index].w, buttons[button_index].h, buttons[button_index].color)
            if not buttons[button_index].filled:
                if buttons[button_index].buttontype == "standard":
                    arcade.draw_rectangle_outline(buttons[button_index].x, buttons[button_index].y, buttons[button_index].w, buttons[button_index].h, buttons[button_index].color)
                elif buttons[button_index].buttontype == "ltrb":
                    arcade.draw_lrtb_rectangle_outline(buttons[button_index].x, buttons[button_index].y, buttons[button_index].w, buttons[button_index].h, buttons[button_index].color)
                elif buttons[button_index].buttontype == "xywh":
                    arcade.draw_xywh_rectangle_outline(buttons[button_index].x, buttons[button_index].y, buttons[button_index].w, buttons[button_index].h, buttons[button_index].color)

    def update_x(buttonid, x):
        button_index = get_button_index_by_id(buttonid)
        if get_button_index_by_id(buttonid) != -1:
            buttons[button_index].x = x
    
    def update_y(buttonid, y):
        button_index = get_button_index_by_id(buttonid)
        if get_button_index_by_id(buttonid) != -1:
            buttons[button_index].y = y
    
    def update_w(buttonid, w):
        button_index = get_button_index_by_id(buttonid)
        if get_button_index_by_id(buttonid) != -1:
            buttons[button_index].w = w
    
    def update_h(buttonid, h):
        button_index = get_button_index_by_id(buttonid)
        if get_button_index_by_id(buttonid) != -1:
            buttons[button_index].h = h
    
    def update_color(buttonid, color):
        button_index = get_button_index_by_id(buttonid)
        if get_button_index_by_id(buttonid) != -1:
            buttons[button_index].color = color
    
    def update_filled(buttonid, filled):
        button_index = get_button_index_by_id(buttonid)
        if get_button_index_by_id(buttonid) != -1:
            buttons[button_index].filled = filled


# Start screen setup
on_start_screen = True
start_key_pressed = False
start_key_rgb = (255, 255, 255)
Button.create(Button("start_button", WIDTH/2, HEIGHT/2, 300, 100, arcade.color.GREEN, True, "standard"))

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
            draw_start_screen_animation()
            if start_key_rgb[0] == 0:
                on_start_screen = False
                on_play_screen = True
    elif on_play_screen:
        draw_grid()


def draw_start_screen():
    Button.draw("start_button")
    arcade.draw_text("PLAY", WIDTH/2 - 60, HEIGHT/2 - 25, arcade.color.WHITE, font_size=50)


def draw_start_screen_animation():
    global start_key_rgb, on_start_screen, on_play_screen
    arcade.draw_xywh_rectangle_filled(0, 0, WIDTH, HEIGHT, start_key_rgb)
    
    if start_key_rgb[0] > 0:
        start_key_rgb = (start_key_rgb[0] - 3, start_key_rgb[1] - 3, start_key_rgb[2] - 3)
    print(start_key_rgb)

    if on_start_screen:
        arcade.set_background_color(arcade.color.WHITE)
    elif on_play_screen:
        arcade.set_background_color(arcade.color.BLACK)


def draw_grid():
    arcade.set_background_color(arcade.color.BLACK)
    arcade.draw_xywh_rectangle_outline(1, 1, WIDTH-1, HEIGHT-2, arcade.color.RED)
    for i in range(int(WIDTH/20)):
        arcade.draw_line(i*20, 0, i*20, HEIGHT, arcade.color.WHITE)
    for i in range(int(HEIGHT/20)):
        arcade.draw_line(0, i*20, WIDTH, i*20, arcade.color.WHITE)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global start_key_pressed
    if WIDTH/2 - 150 <= x <= WIDTH/2 + 150:
        if HEIGHT/2 - 50 <= y <= HEIGHT/2 + 50:
            Button.update_color("start_button", arcade.color.GO_GREEN)
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
