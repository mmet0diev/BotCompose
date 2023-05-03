import os
import sys
# Add the path to the Models directory to the system path
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, "Models"))

from Models.Bot import Bot

# Initialize a bot model
bot = Bot()

def intro() -> str:
    return """
        ||]]]]]]])        ========      ===================
        ||       |)     ||        ||            ||
        ||       |)     ||        ||            ||
        ||       |      ||        ||            ||
        ||]]]]]]|       ||        ||            ||
        ||       |      ||        ||            ||
        ||       |)     ||        ||            ||
        ||       |)     ||        ||            ||
        ||]]]]]]])        ========              ||

           |==========     ========      |\\           /||   ||=======))       ========      ||==========      |========
          ||             ||        ||    || \\        / ||   ||        ))    ||        ||    ||                |
         ||              ||        ||    ||  \\      /  ||   ||        ))    ||        ||    ||                |
        ||               ||        ||    ||    \\   /   ||   ||=======))     ||        ||    ||                |
        ||               ||        ||    ||      \\/    ||   ||              ||        ||    ||=========||     |========
        ||               ||        ||    ||            ||   ||              ||        ||               ||     |
         ||              ||        ||    ||            ||   ||              ||        ||               ||     |
          ||             ||        ||    ||            ||   ||              ||        ||               ||     |
           |==========    ========       ||            ||   ||                ========       ==========||     |========
    """ + "\n"


# Read commands from .txt file
# C:\Users\maxur\Desktop\dsodaily1.txt
def read_from_file(src_file: str):
    print("Press 'esc' to stop command(s) execution.")
    with open(src_file, "r") as f:
        for line in f:
            if bot.kb.check_key_pressed("esc"):
                print("Execution stopped.")
                break
            if line != "":
                cmd1 = line.strip().split(" ")
                func = cmd1[0]
                args = cmd1[1:]
                match func:
                    case "mv":
                        x, y = map(float, args)
                        bot.mv(x, y)
                    case "clck":
                        btn = args[0]
                        bot.clck(btn)
                    case "mvclck":
                        x, y = map(float, args[:2])
                        btn = args[2]
                        bot.mvclck(x, y, btn)
                    case "scroll":
                        n = int(args[0])
                        bot.scroll(n)
                    case "press":
                        key = args[0]
                        bot.press(key)
                    case "hld":
                        comp = args[0]
                        btn = args[1]
                        if comp == 'mouse':
                            bot.mouse_hld(btn=btn)
                        elif comp == 'kb':
                            bot.kb_hld(btn=btn)
                    case "rel":
                        comp = args[0]
                        btn = args[1]
                        if comp == 'mouse':
                            bot.mouse_rel(btn=btn)
                        elif comp == 'kb':
                            bot.kb_rel(btn=btn)
                    case "clckimg":
                        if len(args) == 1:
                            img_path = args[0]
                            bot.clckimg(img_path)
                        elif len(args) == 2:
                            img_path = args[0]
                            btn = args[1]
                            bot.clckimg(img_path, btn=btn)
                        elif len(args) == 3:
                            img_path = args[0]
                            btn = args[1]
                            conf = args[2]
                            bot.clckimg(img_path, btn=btn, conf=conf)
                    case "drag":
                        if(len(args) == 4):
                            x1 = int(args[0])
                            y1 = int(args[1])
                            x2 = int(args[2])
                            y2 = int(args[3])
                            bot.drag(x1, y1, x2, y2)
                        elif(len(args) == 5):
                            x1 = int(args[0])
                            y1 = int(args[1])
                            x2 = int(args[2])
                            y2 = int(args[3])
                            dur = int(args[4])
                            bot.drag(x1, y1, x2, y2, dur)
                        else:
                            print("Invalid arguments passed.")
                    case "wrt":
                        text = " ".join(args)
                        bot.wrt(text)
                    case "sleep":
                        secs = float(args[0])
                        bot.sleep(secs)
                    case "shoot":
                        bot.take_shot()
                    case "repeat":
                        reps = int(args[0])
                        next_lines = int(args[1])
                        bot.repeat_lines(f=f, reps=reps, n_lines=next_lines)
                    case _:
                        print(f"Invalid command(s)/syntax: {func}")
            else:
                print("Empty line")

        f.close()


# Manually issue commands from the terminal(similar to REPL / interactive mode)
def manual_input(cmd: str):
    # cmd = ""
    cmds = cmd.strip().split(" ")
    func = cmds[0]
    args = cmds[1:]
    match func:
        case "mv":
            x, y = map(float, args)
            bot.mv(x, y)
        case "clck":
            btn = args[0]
            bot.clck(btn)
        case "mvclck":
            x, y = map(float, args[:2])
            btn = args[2]
            bot.mvclck(x, y, btn)
        case "scroll":
            n = int(args[0])
            bot.scroll(n)
        case "press":
            btn = args[0]
            bot.press(btn=btn)
        case "hld":
            comp = args[0]
            btn = args[1]
            if comp == 'mouse':
                bot.mouse_hld(btn=btn)
            elif comp == 'kb':
                bot.kb_hld(btn=btn)
        case "rel":
            comp = args[0]
            btn = args[1]
            if comp == 'mouse':
                bot.mouse_rel(btn=btn)
            elif comp == 'kb':
                bot.kb_rel(btn=btn)
        case "clckimg":
            if len(args) == 1:
                img_path = args[0]
                bot.clckimg(img_path)
            elif len(args) == 2:
                img_path = args[0]
                btn = args[1]
                bot.clckimg(img_path, btn=btn)
            elif len(args) == 3:
                img_path = args[0]
                btn = args[1]
                conf = args[2]
                bot.clckimg(img_path, btn=btn, conf=conf)
        case "drag":
            if(len(args) == 4):
                x1 = int(args[0])
                y1 = int(args[1])
                x2 = int(args[2])
                y2 = int(args[3])
                bot.drag(x1, y1, x2, y2)
            elif(len(args) == 5):
                x1 = int(args[0])
                y1 = int(args[1])
                x2 = int(args[2])
                y2 = int(args[3])
                dur = int(args[4])
                bot.drag(x1, y1, x2, y2, dur)
            else:
                print("Invalid arguments passed.")
        case "wrt":
            text = " ".join(args)
            bot.wrt(text)
        case "sleep":
            if len(args) == 0:
                bot.sleep()
            elif len(args) == 1:
                secs = args[0]
                bot.sleep(secs=secs)
        case "shoot":
            bot.take_shot()
        case "repeat":
            if len(args) > 0:
                reps = int(args[0])
                bot.repeat_man(command=cmds[2:], reps=reps)
            else:
                print("Invalid number of args.")
        case "pos":
            print(bot.getPos())
        case _:
            print(f"Invalid command/syntax: {func}")


# def run():
#     print(intro())
#     print('"BotCompose" is a python program designed to "compose bots" or compose commands in order to automate common tasks.')
#     print(
#         "\noptions:\n"
#         "f, file - read commands from a src .txt file\n"
#         "recmouse - start recording mouse events\n"
#         "reckb - start recording keyboard events\n"
#         "playmouse - play the recorded mouse events'\n"
#         "playkb - play the recorded keyboard events'\n"
#         "m, man - enter commands manually(similar to running python intractive terminal)\n"
#         "h, help - Display general info about the tool\n"
#     )
#     # main program loop
#     while True:
#         top_lvl_cmd = input("> ").lower().strip()

#         if top_lvl_cmd == "f" or top_lvl_cmd == "file":
#             try:
#                 src_file = input("Enter src file:\nfile path> ").strip().lower()
#                 if os.path.isfile(f"{src_file}"):
#                     read_from_file(src_file)
#             except Exception:
#                 print(f'{Exception}')
#         elif top_lvl_cmd == "recmouse":
#             print("Recording mouse.\nPress 'esc'(default) to stop.")
#             bot.rec_mouse()
#             print("Recording stopped.")
#         elif top_lvl_cmd == "reckb":
#             print("Recording keyboard.\nPress 'esc'(default) to stop.")
#             bot.rec_kb()
#             print("Recording stopped.")
#         elif top_lvl_cmd == "playmouse":
#             print(f"Playing mouse events:\n")
#             bot.play_mouse()
#             print("Finished.")
#         elif top_lvl_cmd == "playkb":
#             print(f"Playing keyboard events:\n")
#             bot.play_kb()
#             print("Finished.")
#         elif top_lvl_cmd == "m" or top_lvl_cmd == "man":
#             manual_input()
#         elif top_lvl_cmd == "h" or top_lvl_cmd == "help":
#             help()
#         elif top_lvl_cmd == "q" or top_lvl_cmd == "quit" or top_lvl_cmd == "exit":
#             print("Exited\n")
#             exit()
#         else:
#             print('.')


# The help "menu":
# def help():
#     print('\nWelcome to the help menu\n"'
#           'Bot Compose" is a python program designed to "compose" "bots" and automate various tasks\n'
#           'Using this tool, the user is able to control the mouse/keyboard in various ways using the\n'
#             'mouse/keyboard commands available from the bot model.\n'
#             'The most common functions the Model offers include the mouse functions:\n'
#         'mv(x, y), clck(btn=l r m), mvclck(x, y, btn),\n as well as keyboard functions:\n'
#         'press(btn), hld(btn), rel(btn), wrt(text), and other useful functions like sleep(time), record actions,\n'
#         'There are various ways these functions can be composed together to create a sequence of actions to be automated.'
#         'reading commands from a file example:\n'
#         'sleep 5\nmv 200 120\nsleep 1\nclck l\nclck l\nmvclck 340 215 l\nwrt Hello World!\npress tab\n my name is Jack.\n'
#         'The bot also has functions such as rec() for mouse/keyboard events recording, play() for playing recorded events,\n'
#         'repeat() for repeating a sequence of events/actions which can be utilized throught read_from_file or manual_input\n'
#         'more on them later.'
#     )
#     print(
#         "options:"
#         "f, file - read commands from a src .txt file\n"
#         "recmouse - start recording mouse events\n"
#         "reckb - start recording keyboard events\n"
#         "playmouse - replay recorded mouse events\n"
#         "playkb - replay recorded keyboard events\n"
#         "m, man - enter commands manually(similar to running python intractive terminal)\n"
#         "h, help - Display general info about the tool\n"
#     )
#     print(
#         "This tool can be used in numerous ways and the effective usage of it is dependent on the user's imagination.")
#     print(
#         "The the core concept of this botcomposition/automation program is for it to execute 'commands' set by the user.\n"
#     )

import tkinter as tk

class AppUI():
    def __init__(self, bot=Bot()) -> None:
        self.bot = bot
        self.root = tk.Tk()
        self.root.title("Bot Controller")
        self.root.geometry("600x350")
        self.root.resizable(False, False)
        self.root.columnconfigure([0,1,2,3], pad=20)
        self.root.rowconfigure([0,1,2,3], pad=20)

        # Define widgets
        bot_label = tk.Label(self.root, text="BOTCOMPOSE", font=("Helvetica", 20), pady=5)
        mouse_rec_btn = tk.Button(self.root, text="rec mouse", pady=5, command=self.bot.rec_mouse)
        kb_rec_btn = tk.Button(self.root, text="rec kb", pady=5, command=self.bot.rec_kb)
        mouse_play_btn = tk.Button(self.root, text="play mouse", pady=5, command=self.bot.play_mouse)
        kb_play_btn = tk.Button(self.root, text="play kb", pady=5, command=self.bot.play_kb)

        file_read_label = tk.Label(self.root, text="Read from file ->")
        file_read_btn = tk.Button(self.root, text="src file", pady=5)

        manual_label = tk.Label(self.root, text="Run commands manually ->")
        input_field = tk.Entry(self.root)
        man_run_btn = tk.Button(self.root, text="Run")

        # Pack widgets
        bot_label.grid(row=0, column=0, columnspan=4) # span across all columns
        mouse_rec_btn.grid(row=1, column=0)
        kb_rec_btn.grid(row=1, column=1)
        mouse_play_btn.grid(row=1, column=2)
        kb_play_btn.grid(row=1, column=3)
        file_read_label.grid(row=2, column=0)
        file_read_btn.grid(row=2, column=1)
        manual_label.grid(row=3, column=0)
        input_field.grid(row=3, column=1)
        man_run_btn.grid(row=3, column=2)

        # Center the bot_label widget
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        bot_label.grid_configure(sticky="nsew")

        self.root.mainloop()


def run():
    app = AppUI(bot=bot)

if __name__ == "__main__":
    run()
