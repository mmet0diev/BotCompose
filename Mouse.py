import mouse as m
import keyboard as kb
import time
import os


class Mouse:

    def __init__(self, 
                 comp_name="mouse", 
                 events=[], 
                 output_file="mouse_events.txt") -> None:
        self.comp_name = comp_name
        self.events = events
        self.output_file = output_file
        self.pos = m.get_position()


    # Mouse controls:
    # More of a testing func
    def getPos(self):
        return m.get_position()

    # Move the mouse to xy
    def mv(self, x: int, y: int, dur=0):
        # print("mv called")
        m.move(x, y, duration=dur)

    # Click a left, right, middle(scroll) mouse btn
    def clck(self, btn: str):
        time.sleep(0.2)
        if (btn == "l"):
            m.click()
        elif (btn == "r"):
            m.right_click()
        elif (btn == "m"):
            m.click(button="middle")
        else:
            print("Invalid mouse btn.")

    # A combination of mv() and clck()
    def mvclck(self, x: int, y: int, btn: str):
        time.sleep(0.2)
        if (btn == "l"):
            m.move(x, y)
            time.sleep(0.1)
            m.click()
        elif (btn == "r"):
            m.move(x, y)
            time.sleep(0.1)
            m.right_click()
        elif (btn == "m"):
            m.move(x, y)
            time.sleep(0.1)
            m.click(button="middle")
        else:
            print("Unknown mouse btn.")

    # Scroll the scroller z units + for up - for down
    def scroll(self, z: int):
        m.wheel(z)

    # Hold a given mouse btn
    def hld(self, btn: str):
        m.press(btn)

    # Release a given mouse btn
    def rel(self, btn: str):
        if m.is_pressed(btn):
            m.release(btn)


    def write_to_file(self):
        with open(self.output_file, 'w') as f:
            for evs in self.events:
                f.write(f"{evs}\n")
            f.close()


    def clear_file(self, file_path):
        open(file_path, 'w').close()


    def stop_recording(self):
        kb.wait('esc')
        m.unhook_all()


    def record(self):
        self.events = []
        self.clear_file(self.output_file)
        self.pos = self.getPos()
        m.hook(self.events.append)
        self.stop_recording()
        self.write_to_file()


    def play(self):
        time.sleep(1)
        m.move(x=self.pos[0], y=self.pos[1])
        m.play(self.events, speed_factor=1)


    def __str__(self) -> str:
         return f"Component: {self.comp_name}"
    

