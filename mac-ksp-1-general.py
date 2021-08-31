# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "KSP General",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000202, "kOS", ["5"]),
        (0x020200, "RCS", ["r"]),
        (0x040404, "SAS", ["t"]),
        # 2nd row ---------
        (0x020200, "Gear", ["g"]),
        (0x020200, "Brakes", ["b"]),
        (0x000202, "Qsave", [Keycode.F5]),
        # 3rd row ----------
        (0x000200, "Full", ["z"]),
        (0x010201, "T-up", [Keycode.LEFT_SHIFT]),
        (0x000202, "Qload", [Keycode.F9]),
        # 4th row ----------
        (0x020000, "Cutoff", ["x"]),
        (0x020101, "T-down", [Keycode.LEFT_CONTROL]),
        (0x020202, "Fine", [Keycode.RETURN]),
        # Encoder button ---
        (0x000000, "Stage", [" "]),
    ],
}
