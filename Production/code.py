print("Starting")

# Import
import board
import busio

# KMK Core
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# RGB LEDs
from kmk.extensions.rgb import RGB

# Rotary Encoder
from kmk.modules.encoder import EncoderHandler, Encoder

# OLED Display
from kmk.extensions.oled import OLED, TextEntry

keyboard = KMKKeyboard()

# Matrix Configuration
keyboard.col_pins = (board.GP29, board.GP0, board.GP1)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# OLED Display Setup

i2c = busio.I2C(scl=board.GP7, sda=board.GP6)

oled = OLED(
    i2c=i2c,
    width=128,
    height=32,
    entries=[
        TextEntry(text="Keep Going!", x=0, y=0),
        TextEntry(text="Never Settle", x=0, y=16),
    ]
)

keyboard.extensions.append(oled)

# RGB LED Setup
rgb = RGB(
    pixel_pin=board.GP2,
    num_pixels=9,
)

keyboard.extensions.append(rgb)

# Rotary Encoder Setup
encoder_handler = EncoderHandler()

encoder_handler.encoders = (
    Encoder(
        pin_a=board.GP3,
        pin_b=board.GP4,
    ),
)

# Mapping Encoder rotation to Volume Up / Down
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),  # (Clockwise, Counter-Clockwise)
]

keyboard.modules.append(encoder_handler)

# Keymap Configuration
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
    ]
]

# Run Keyboard
if __name__ == '__main__':
    keyboard.go()
