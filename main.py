import os
from  tcod import libtcodpy as libcod

data_folder = 'data'
font = os.path.join(data_folder, 'font.png')


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    libcod.console_set_custom_font(font, libcod.FONT_TYPE_GRAYSCALE | libcod.FONT_LAYOUT_TCOD)
    libcod.console_init_root(screen_width, screen_height, "game", False)
    con = libcod.console_new(screen_width, screen_height)
    
    key = libcod.Key()
    mouse = libcod.Mouse()

    while not libcod.console_is_window_closed():
        
        libcod.sys_check_for_event(libcod.EVENT_KEY_PRESS, key, mouse)
        libcod.console_set_default_foreground(con, libcod.white)
        libcod.console_put_char(con, player_x, player_y, "@", libcod.BKGND_DEFAULT)
        libcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)
        libcod.console_flush()

        libcod.console_put_char(con, player_x, player_y, " ", libcod.BKGND_NONE)

        if key.vk == libcod.KEY_ESCAPE:
            return True
        if key.vk == libcod.KEY_UP:
            player_y -= 1
        elif key.vk == libcod.KEY_DOWN: 
            player_y += 1
        elif key.vk == libcod.KEY_LEFT: 
            player_x -=1
        elif key.vk == libcod.KEY_RIGHT: 
           player_x += 1

if __name__ == '__main__':
    main()