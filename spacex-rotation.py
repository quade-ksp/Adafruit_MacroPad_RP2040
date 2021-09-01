# Adafruit MacroPad RP2040 - Macros to control the SpaceX ISS Docking Simulator in Internet Brower
# Navigate to https://iss-sim.spacex.com and have fun!

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    'name' : 'Dragon Rotation', # Application name
    'macros' : [   # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', ['']),
        (0x000000, '', ['']),
        (0x000000, '', ['']),
        # 2nd row ---------
        (0x000202, 'CntrClk', [","]),
        (0x020200, 'Up', [Keycode.UP_ARROW]),
        (0x000202, 'Clock', ['.']),
        # 3rd row ----------
        (0x020200, '<Left', [Keycode.LEFT_ARROW]),
        (0x000200, 'Fine', ['']),
        (0x020200, 'Right>', [Keycode.RIGHT_ARROW]),
        # 4th row ----------
        (0x000000, '', ['']),
        (0x020200, 'Down', [Keycode.DOWN_ARROW]),
        (0x000000, '', ['']),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
