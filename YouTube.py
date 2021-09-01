# Adafruit MacroPad RP2040 - Macros to control YouTube in Internet Brower

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    'name' : 'YouTube', # Application name
    'macros' : [   # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x020000, 'Mute', ['m']),                  # Toggles Mute
        (0x020200, 'Full', ['f']),                  # Toggle Full Screen Mode
        (0x020200, 'Caption', ['c']),               # Toggles Captions
        # 2nd row ---------
        (0x000202, '<Prev', [Keycode.SHIFT, 'p']),  # If in Playlist goes to previous video in playlist, else inop
        (0x020200, 'Theater', ['t']),               # Toggle Theater Mode
        (0x000202, 'Next>', [Keycode.SHIFT, 'n']),  # If in Playlist goes to next video in playlist, else next suggested video
        # 3rd row ----------
        (0x000202, '<5s', [Keycode.LEFT_ARROW]),    # Skips back five seconds
        (0x000400, 'Play', ['k']),                  # Toggles Play
        (0x000202, '5s>', [Keycode.RIGHT_ARROW]),   # Skips forward five seconds
        # 4th row ----------
        (0x000202, '<1F', [',']),                   # If paused skips backward 1 frame
        (0x020200, 'Mini', ['i']),                  # Toggles MiniPlayer
        (0x000202, '1F>', ['.']),                   # If paused skips forward 1 frame
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
