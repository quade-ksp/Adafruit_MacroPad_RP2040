# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "KSP kOS Programs",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000202, "kOS", ["5"]),
        (0x000202, "Reboot", ["reboot."]),
        (0x020202, "Clear", ["clearscreen.", Keycode.ENTER]),
        # 2nd row ---------
        (0x000200, "Dalign", ["run dalign."]),
        (0x000200, "Desc", ["run desc."]),
        (0x000200, "NdBurn", ["run nodeburn."]),
        # 3rd row ----------
        (0x020200, "Rndvs", ["run rend."]),
        (0x020200, "Rnd30", ['run rend30.']),
        (0x020200, "Rnd40", ["run rend40."]),
        # 4th row ----------
        (0x040000, "RETRO", ["run retro."]),
        (0x040000, "Rtr150", ['run retro150.']),
        (0x040000, "Rtr155", ['run retro155.']),
        # Encoder button ---
        (0x000000, "Enter", [Keycode.ENTER]),
    ],
}
