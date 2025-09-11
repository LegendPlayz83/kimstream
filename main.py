from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
import board

keyboard = KMKKeyboard()

keyboard.row_pins = []
keyboard.col_pins = []
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.direct_pins = [
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
    board.GP6,
    board.GP7,
]

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP0, board.GP1, board.GP2),)
keyboard.modules.append(encoder_handler)

keyboard.keymap = [
    [
        KC.W,
        KC.A,
        KC.S,
        KC.D,
        KC.E,
        KC.SLSH,
    ]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

if __name__ == '__main__':
    keyboard.go()
