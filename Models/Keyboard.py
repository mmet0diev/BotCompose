import keyboard as kb
import time
import os

class Keyboard:

    hotkeys = []

    # The KB constructor
    def __init__(self, comp_name="KB", 
                 events=[], 
                 output_file="txt/kb_events.txt",
                 hotkeys = []) -> None:
        self.comp_name = comp_name
        self.events = events
        self.output_file = output_file
        self.hotkeys = hotkeys

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

    # Clear the KB file contents
    def clear_file(self, file_path: str):
        if os.path.isfile(file_path):
            open(file_path, 'w').close()

    # Write to the output file
    def write_to_file(self):
        with open(self.output_file, 'w') as f:
            for evs in self.events:
                f.write(f"{evs}\n")
            f.close()

    # Stop recording the keyboard events
    def stop_recording(self):
        kb.wait('esc')
        kb.unhook_all()

    # Record the keyboard events
    def record(self):
        self.events = []
        self.clear_file(self.output_file)
        kb.hook(self.events.append)
        self.stop_recording()
        self.write_to_file()

    # Play the keyboard events
    def play(self):
        time.sleep(1)
        kb.play(self.events)

    # Check if a key is pressed
    def check_key_pressed(self, key: str):
        if kb.is_pressed(key):
            return True
        return False

    # Add a hotkey
    def add_hk(self, hk: str="h+k", callback=None, args=()):
        if callback is None:
            callback = lambda: print(self.__str__())
        try:
            kb.add_hotkey(hk, callback, args)
            self.hotkeys.append(hk)
            print(f"Added hotkey {hk}")
        except ValueError:
            print(f"Hotkey {hk} already added")

    # Remove a hotkey
    def rm_hk(self, hk: str):
        try:
            kb.remove_hotkey(hk)
            self.hotkeys.remove(hk)
            print(f"Removed hotkey {hk}")
        except:
            print(f"hotkey combo {hk} not added")

    # toString of KB
    def __str__(self) -> str:
         return f"Component: {self.comp_name}\nAdded hotkeys:{self.hotkeys}"
    