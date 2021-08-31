# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "KSP EVA Surface",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000202, "Board", ["b"]),
        (0x020000, "Release", [" "]),
        (0x000000, "", [""]),
        # 2nd row ---------
        (0x000000, "", [""]),
        (0x020200, "Fwd", ["w"]),
        (0x000000, "", [""]),
        # 3rd row ----------
        (0x020200, "< T", ["a"]),
        (0x000200, "Use", ["f"]),
        (0x020200, "T >", ["d"]),
        # 4th row ----------
        (0x000000, "", [""]),
        (0x020200, "Bkwd", ["s"]),
        (0x020202, "Fine", [Keycode.RETURN]),
        # Encoder button ---
        (0x000000, "", ["u"]),
    ],
}
