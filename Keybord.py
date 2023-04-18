import keyboard as kb
import time
import os


class KB:

    comp_name: str
    events: list
    output_file: str


    def __init__(self, comp_name="keyboard", events=[], output_file="kb_events.txt") -> None:
        self.comp_name = comp_name
        self.events = events
        self.output_file = output_file


    # Press a given btn
    def press(self, btn: str):
        time.sleep(0.1)
        kb.press(btn)
        kb.release(btn)

    # Holds a given btn
    def hld(self, btn: str):
        kb.press(btn)

    # Releases a given btn
    def rel(self, btn: str):
        kb.release(btn)

    # Press and release a sequence of keys/btns
    def wrt(self, text: str, d: int = 0.1):
        time.sleep(1)
        kb.write(text, delay=d)

    def clear_file(self, file_path: str):
        if os.path.isfile(file_path):
            open(file_path, 'w').close()

    def write_to_file(self):
        with open(self.output_file, 'w') as f:
            for evs in self.events:
                f.write(f"{evs}\n")
            f.close()

    def stop_recording(self):
        kb.wait('esc')
        kb.unhook_all()

    def record(self):
        self.events = []
        self.clear_file(self.output_file)
        kb.hook(self.events.append)
        self.stop_recording()
        self.write_to_file()

    def play(self):
        time.sleep(1)
        kb.play(self.events)

    def __str__(self) -> str:
         return f"Component: {self.comp_name}"