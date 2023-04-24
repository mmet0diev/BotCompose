import os
import time
from Models.Keyboard import Keyboard
from Models.Mouse import Mouse
import pyautogui as pag

class Bot:

    imgs_path = os.path.join(os.getcwd(), "imgs")

    # get initial number of image files in imgs folder
    def get_imgs_num(self) -> int:
        imgs_list = os.listdir(self.imgs_path)
        return len(imgs_list)
    
    # Bot constructor
    def __init__(
        self,
        comp_name="Bot",
        events=[],
        m=Mouse(),
        kb=Keyboard(),
        imgs_num=None
    ) -> None:
        self.comp_name = comp_name
        self.events = events
        self.m = m
        self.kb = kb
        if imgs_num is None:
            self.imgs_num = self.get_imgs_num()
        else:
            self.imgs_num = imgs_num

    # Mouse controls:
    # More of a testing function
    def getPos(self):
        return self.m.getPos()

    # Move the mouse to xy
    def mv(self, x: int, y: int, dur=0):
        # print("mv called")
        self.m.mv(x=x, y=y, dur=dur)

    # Click a left, right, middle(scroll) mouse btn
    def clck(self, btn: str):
        self.m.clck(btn=btn)

    # A combination of mv() and clck()
    def mvclck(self, x: int, y: int, btn: str):
        self.m.mvclck(x=x, y=y, btn=btn)

    # Scroll the scroller z units + for up - for down
    def scroll(self, z: int):
        self.m.scroll(z=z)

    # Hold a given mouse btn
    def mouse_hld(self, btn: str):
        self.m.hld(btn=btn)
    
    # Drag the mouse to chosen coords
    def drag(self, x1, y1, x2, y2, dur):
        self.m.drag(x1=x1, y1=y1, x2=x2, y2=y2, dur=dur)

    # Release a given mouse btn
    def mouse_rel(self, btn: str):
        self.m.rel(btn=btn)

    # Hold a given keyboard btn
    def kb_hld(self, btn: str):
        self.kb.hld(btn=btn)

    # Release a given keyboard btn
    def kb_rel(self, btn: str):
        self.kb.rel(btn=btn)

    # Keyboard controls:
    # Press a key/btn
    def press(self, btn: str):
        self.kb.press(btn=btn)

    # Press and release a sequence of keys/btns
    def wrt(self, text: str, d: int = 0.1):
        self.kb.wrt(text=text, d=d)

    # Puts the bot in "sleep" for secs time

    def sleep(self, secs=2.0):
        time.sleep(secs)

    # Repeats a sequence of commands
    def repeat(self, commands: list[str] = [], reps: int = 2, n_lines: int = 1, start_index: int = 0):
        time.sleep(1)
        for i in range(reps):
            index = start_index
            while index < len(commands):
                cmd = commands[index]
                if cmd == "mv":
                    coords = (commands[index + 1], commands[index + 2])
                    x = float(coords[0])
                    y = float(coords[1])
                    self.mv(x=x, y=y)
                    index += 3
                elif cmd == "clck":
                    btn = commands[index + 1]
                    self.clck(btn=btn)
                    index += 2
                elif cmd == "mvclck":
                    coords = (commands[index + 1], commands[index + 2])
                    x = float(coords[0])
                    y = float(coords[1])
                    btn = commands[index + 3]
                    self.mvclck(x=x, y=y, btn=btn)
                    index += 4
                elif cmd == "scroll":
                    n = int(commands[index + 1])
                    self.scroll(n)
                    index += 2
                elif cmd == "press":
                    key = commands[index + 1]
                    self.press(key)
                    index += 2
                elif cmd == "hld":
                    key = commands[index + 1]
                    self.hld(key)
                    index += 2
                elif cmd == "rel":
                    key = commands[index + 1]
                    self.rel(key)
                    index += 2
                elif cmd == "wrt":
                    text = " ".join(commands[index + 1:])
                    self.wrt(text)
                    break
                elif cmd == "sleep":
                    secs = float(commands[index + 1])
                    self.sleep(secs)
                    index += 2
                elif cmd == "repeat":
                    sub_commands = commands[index + 1:index + 1 + n_lines]
                    sub_reps = int(commands[index + 1 + n_lines])
                    self.repeat(sub_commands, reps=sub_reps, n_lines=n_lines, start_index=index+1)
                    index += n_lines + 2
                else:
                    index += 1

    # Call the record function from the Mouse
    def rec_mouse(self):
        self.m.record()

    # Call the play function from the Mouse
    def play_mouse(self):
        self.m.play()

    # Call the record function from KB
    def rec_kb(self):
        self.kb.record()

    # Call the play function from KB
    def play_kb(self):
        self.kb.play()

    def take_shot(self, trig: str):
        pag.screenshot(f"{self.imgs_path}\\screenshot{self.imgs_num}.png")
        self.imgs_num+=1

    # toString for Model (Bot)
    def __str__(self) -> str:
        return f"Component: {self.comp_name}"
