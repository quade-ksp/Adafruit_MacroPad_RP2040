# Adafruit MacroPad RP2040 - Macros to control the SpaceX ISS Docking Simulator in Internet Brower
# Navigate to https://iss-sim.spacex.com and have fun!

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    'name' : 'Dragon Translation', # Application name
    'macros' : [   # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', ['']),
        (0x000000, '', ['']),
        (0x000000, '', ['']),
        # 2nd row ---------
        (0x000202, 'Fwd', ['e']),
        (0x020200, 'Up', ['w']),
        (0x000000, '', ['']),
        # 3rd row ----------
        (0x020200, '<Left', ['a']),
        (0x000200, 'Fine', ['']),
        (0x020200, 'Right>', ['d']),
        # 4th row ----------
        (0x000202, 'Bkwrd', ['q']),
        (0x020200, 'Down', ['s']),
        (0x000000, '', ['']),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
