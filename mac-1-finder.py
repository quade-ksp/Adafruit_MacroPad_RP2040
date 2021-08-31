# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    'name' : 'Finder',  # Application name
    'macros' : [   # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000004, 'Safari', [Keycode.COMMAND, ' ', 0.5, 'Safari.app', 0.1, Keycode.RETURN]),
        (0x020000, 'New', [Keycode.COMMAND, "n"]),
        (0x000202, 'Siri', [Keycode.CONTROL, Keycode.COMMAND, ' ']),
        # 2nd row ---------
        (0x000004, 'Notes', [Keycode.COMMAND, ' ', 0.5, 'Notes.app', 0.1, Keycode.RETURN]),
        (0x020000, 'NewTab', [Keycode.COMMAND, "t"]),
        (0x000202, 'Dict', [Keycode.CONTROL, "d"]),
        # 3rd row ----------
        (0x000004, 'Mu Edit', [Keycode.COMMAND, ' ', 0.5, 'Mu Editor', 0.1, Keycode.RETURN]),
        (0x000004, 'KSP', [Keycode.COMMAND, ' ', 0.5, 'KSP', 0.1, Keycode.RETURN]),
        (0x020200, 'FGrab', [Keycode.COMMAND, Keycode.SHIFT, "3"]),
        # 4th row ----------
        (0x000004, 'Mssgs', [Keycode.COMMAND, ' ', 0.5, 'Messages.app', 0.1, Keycode.RETURN]),
        (0x000004, 'Calc', [Keycode.COMMAND, ' ', 0.5, 'Calculator.app', 0.1, Keycode.RETURN]),
        (0x020200, 'SShot', [Keycode.COMMAND, ' ', 0.5, 'Screenshot.app', 0.1, Keycode.RETURN]),
        # Encoder button ---
        (0x000000, '', [''])
    ]
}
