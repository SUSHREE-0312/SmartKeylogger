from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlMouse():
    mouse = Controller()
    mouse.position = (100,20)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("I am yours.")

controlKeyboard()