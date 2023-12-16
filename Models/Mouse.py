import mouse as m
import keyboard as kb
import time
import os
import pyautogui as pag


class Mouse:

    # The Mouse constructor
    def __init__(self,
            comp_name="Mouse",
            events=[],
            output_file="txt/mouse_events.txt") -> None:
        self.comp_name = comp_name
        self.events = events
        self.output_file = output_file
        self.pos = m.get_position()

    # Mouse controls:
    # Get mouse position
    def getPos(self):
        self.pos = m.get_position()
        return f"Mouse coordinates: {self.pos}"
        # while True:
        #     new_x, new_y = m.get_position()[0], m.get_position()[1]
        #     if self.pos[0] != new_x and self.pos[1] != new_y:
        #         print(f"Coords: {new_x}, {new_y}")
        #         time.sleep(0.1)

    # Move the mouse to xy  
    def mv(self, x: int, y: int, dur=0):
        # print("mv called")
        time.sleep(0.1)
        m.move(x, y, duration=dur, absolute=True)

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
            m.move(x, y, duration=0, absolute=True)
            time.sleep(0.1)
            m.click()
        elif (btn == "r"):
            m.move(x, y, duration=0, absolute=True)
            time.sleep(0.1)
            m.right_click()
        elif (btn == "m"):
            m.move(x, y, duration=0, absolute=True)
            time.sleep(0.1)
            m.click(button="middle")
        else:
            print("Unknown mouse btn.")

    # Scroll the scroller z units + for up - for down
    def scroll(self, z: int):
        time.sleep(0.2)
        m.wheel(z)

    # Hold a given mouse btn
    def hld(self, btn: str):
        time.sleep(0.2)
        m.press(button=btn)

    # Release a given mouse btn
    def rel(self, btn: str):
        if m.is_pressed(btn):
            m.release(btn)

    # Drag the mouse from starting point (x1, y2) to end point (x2, y2)
    def drag(self, x1, y1, x2, y2, dur=1):
        time.sleep(0.5)
        m.drag(start_x=x1, start_y=y1, end_x=x2,
               end_y=y2, absolute=True, duration=dur)

    # Move the mouse and click an image
    def clck_img(self, img: str, btn: str="l", conf=0.6):
        time.sleep(0.2)
        try:
            img_location = pag.locateOnScreen(img, confidence=conf)
            img_center: tuple = None
            if(img is not None):
                img_center = pag.center(img_location)
                print(img_center)
            else:
                print("Image not found.")
                return
            self.mvclck(img_center[0], img_center[1], btn=btn)
        except Exception as e:
            print(f"Exception caught:\n {e}")

    # Write to mouse events output.txt file
    def write_to_file(self):
        if os.path.isfile(self.output_file):
            with open(self.output_file, 'w') as f:
                for evs in self.events:
                    f.write(f"{evs}\n")

    # Clear the current output.txt contents
    def clear_file(self):
        open(self.output_file, 'w').close()

    # Stop recording the mouse events
    def stop_recording(self):
        kb.wait('esc')
        m.unhook_all()

    # Record the mouse events
    def record(self):
        m.unhook_all()
        self.events = []
        self.clear_file()
        self.pos = m.get_position()
        m.hook(self.events.append)
        self.stop_recording()
        self.write_to_file()

    # Play the mouse events
    def play(self):
        time.sleep(1)
        m.move(x=self.pos[0], y=self.pos[1])
        m.play(self.events, speed_factor=1)

    # toString of Mouse
    def __str__(self) -> str:
        return f"Component: {self.comp_name}"
