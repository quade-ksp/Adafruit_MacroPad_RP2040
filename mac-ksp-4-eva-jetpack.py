# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "KSP EVA Jetpack",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000202, "< Y", ["q"]),
        (0x020000, "Release", [" "]),
        (0x000202, "Y >", ["e"]),
        # 2nd row ---------
        (0x000004, "Up", ["h"]),
        (0x020200, "Fwd", ["i"]),
        (0x020202, "JetPk", ["r"]),
        # 3rd row ----------
        (0x020200, "< T", ["j"]),
        (0x000200, "Use", ["f"]),
        (0x020200, "T >", ["l"]),
        # 4th row ----------
        (0x000004, "Down", ["n"]),
        (0x020200, "Bkwd", ["k"]),
        (0x020202, "Fine", [Keycode.RETURN]),
        # Encoder button ---
        (0x000000, "", ["u"]),
    ],
}
