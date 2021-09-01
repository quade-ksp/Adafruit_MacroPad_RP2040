# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    'name' : 'YouTube', # Application name
    'macros' : [   # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x020000, 'Mute', ['m']),
        (0x020200, 'Full', ['f']),
        (0x020200, 'Caption', ['c']),
        # 2nd row ---------
        (0x000202, '<Prev', [Keycode.SHIFT, 'p']),
        (0x020200, 'Theater', ['t']),
        (0x000202, 'Next>', [Keycode.SHIFT, 'n']),
        # 3rd row ----------
        (0x000202, '<5s', [Keycode.LEFT_ARROW]),
        (0x000400, 'Play', ['k']),
        (0x000202, '5s>', [Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0x000202, '<1F', [',']),
        (0x020200, 'Mini', ['i']),
        (0x000202, '1F>', ['.']),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
