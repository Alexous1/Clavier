# Imports
import time
import usb_hid
import board

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialise keyboard
keyboard = Keyboard(usb_hid.devices)

# Definit les diférentes scénes
hid_actions = [
    {
        "name": "Scene 1",
        "held": False,
        "keycode": (Keycode.SHIFT,Keycode.PERIOD, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        #slash inversé
        "name": "Scene 2",
        "held": False,
        "keycode": (Keycode.SHIFT,Keycode.PERIOD, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        #page web avance
        "name": "Scene 3",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.RIGHT_ARROW),
        "button": None,
        "led": None,
    },
    {
        #page web retour
        "name": "Scene 4",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.LEFT_ARROW),
        "button": None,
        "led": None,
    },
    {
        #crochet gauche
        "name": "Scene 5",
        "held": False,
        "keycode": (Keycode.SHIFT,Keycode.FIVE, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        #crochet droite
        "name": "Scene 6",
        "held": False,
        "keycode": (Keycode.SHIFT,Keycode.MINUS, Keycode.ALT),
        "button": None,
        "led": None,
    },
    {
        # capture d'ecan
        "name": "Scene 7",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.SHIFT, Keycode.THREE),
        "button": None,
        "led": None,
    },
    {
        # éteindre ecran””
        "name": "Scene 8",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.CONTROL, Keycode.A),
        "button": None,
        "led": None,
    },
    {
        #coller
        "name": "Scene 9",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.V),
        "button": None,
        "led": None,
    },
    {
        # copier
        "name": "Scene 10",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.C),
        "button": None,
        "led": None,
    },
    {
        #new fenetre
        "name": "Scene 11",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.T),
        "button": None,
        "led": None,
    },
    {
        # delete fenetre
        "name": "Scene 12",
        "held": False,
        "keycode": (Keycode.GUI, Keycode.Z),
        "button": None,
        "led": None,
    },
]


# Definit les buttons pins
btn_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
]

# Definit les leds pins
led_pins = [
    board.GP13,
    board.GP14,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
    board.GP28,
]

# Setup tous les butons
# Setup toutes les leds
for i in range(12):
    button = DigitalInOut(btn_pins[i])
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    hid_actions[i]["button"] = button

    led = DigitalInOut(led_pins[i])
    led.direction = Direction.OUTPUT
    hid_actions[i]["led"] = led

# loop
while True:

    for i in range(12):

        # vérifie si un bouton est pressé
        if not hid_actions[i]["button"].value and not hid_actions[i]["held"]:

            # print le nom de la scéne
            print(hid_actions[i]["name"])

            # envoie les touches pressé aux keyboard
            keyboard.send(*hid_actions[i]["keycode"])

            # allume la leds concerné
            hid_actions[i]["led"].value = True

            # met les autres les en false
            for j in range(12):
                if i != j:
                    hid_actions[j]["led"].value = False

            # met held en true
            hid_actions[i]["held"] = True

        # remove held
        elif hid_actions[i]["button"].value and hid_actions[i]["held"]:
            hid_actions[i]["held"] = False
