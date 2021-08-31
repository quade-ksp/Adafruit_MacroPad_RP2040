# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "KSP Fine RCS",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000202, "Dalign", ["5", 0.5, "Run Dalign.", Keycode.RETURN]),
        (0x020200, "RCS", ["r"]),
        (0x000000, "", [""]),
        # 2nd row ---------
        (0x000004, "+Z", ["h"]),
        (0x020200, "+Y", ["i"]),
        (0x000000, "", [""]),
        # 3rd row ----------
        (0x020200, "-X", ["j"]),
        (0x000000, "", [""]),
        (0x020200, "+X", ["l"]),
        # 4th row ----------
        (0x000004, "-Z", ["n"]),
        (0x020200, "-Y", ["k"]),
        (0x020202, "Fine", [Keycode.RETURN]),
        # Encoder button ---
        (0x000000, "", ["u"]),
    ],
}
