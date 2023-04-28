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
                        key = args[0]
                        bot.rel(key)
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
                        commands = []  # initialize the repeated commands list
                        reps = int(args[0])  # parse the repetitions parameter
                        lines = int(args[1])
                        for i in range(lines):  # read the next n lines of commands
                            line = next(f).strip() # read the current line as str
                            cmd2 = line.strip().split(" ")
                            func = cmd2[0]
                            args = cmd2[1:]
                            commands.append((func, args))
                        for j in range(reps):  # repeat the commands reps times
                            for func, args in commands:
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
                                        key = args[0]
                                        bot.hld(key)
                                    case "rel":
                                        key = args[0]
                                        bot.rel(key)
                                    case "wrt":
                                        text = " ".join(args)
                                        bot.wrt(text)
                                    case "sleep":
                                        secs = float(args[0])
                                        bot.sleep(secs)
                                    case "shoot":
                                        bot.take_shot()
                                    case "repeat":
                                        print("Cannot nest more repeat commands")
                                    case _:
                                        print(f"Invalid command: {func}")
                    case _:
                        print(f"Invalid command(s)/syntax: {func}")
            else:
                print("Empty line")

        f.close()


# Manually issue commands from the terminal(similar to REPL / interactive mode)
def manual_input():
    cmd = ""
    print("Manual commands input:\n [s | q | stop | quit] to stop manual mode.\n")
    while True:
        cmd = input("manual> ")
        try:
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
                    case "repeat":
                        if len(args) > 0:
                            if isinstance(args[0], int):
                                r = int(args[0])
                                bot.repeat(commands=cmds[2:], reps=r)
                            elif isinstance(args[0], str):
                                bot.repeat(commands=cmds[1:])
                        else:
                            print("No command to repeat given")
                    case "shoot":
                        bot.take_shot()
                    case "pos":
                        print(bot.getPos())
                    case "q":
                        break
                    case "quit":
                        break
                    case "s":
                        break
                    case "stop":
                        break
                    case _:
                        print(f"Invalid command/syntax: {func}")
        except Exception as e:
            print(f"Invalid commands syntax:\n{e}")


def run():
    print(intro())
    print('"BotCompose" is a python program designed to "compose bots" or compose commands in order to automate common tasks.')
    print(
        "\noptions:\n"
        "f, file - read commands from a src .txt file\n"
        "recmouse - start recording mouse events\n"
        "reckb - start recording keyboard events\n"
        "playmouse - play the recorded mouse events'\n"
        "playkb - play the recorded keyboard events'\n"
        "m, man - enter commands manually(similar to running python intractive terminal)\n"
        "h, help - Display general info about the tool\n"
    )
    # main program loop
    while True:
        top_lvl_cmd = input("> ").lower().strip()

        if top_lvl_cmd == "f" or top_lvl_cmd == "file":
            try:
                src_file = input("Enter src file:\nfile path> ").strip().lower()
                if os.path.isfile(f"{src_file}"):
                    read_from_file(src_file)
            except Exception:
                print(f'{Exception}')
        elif top_lvl_cmd == "recmouse":
            print("Recording mouse.\nPress 'esc'(default) to stop.")
            bot.rec_mouse()
            print("Recording stopped.")
        elif top_lvl_cmd == "reckb":
            print("Recording keyboard.\nPress 'esc'(default) to stop.")
            bot.rec_kb()
            print("Recording stopped.")
        elif top_lvl_cmd == "playmouse":
            print(f"Playing mouse events:\n")
            bot.play_mouse()
            print("Finished.")
        elif top_lvl_cmd == "playkb":
            print(f"Playing keyboard events:\n")
            bot.play_kb()
            print("Finished.")
        elif top_lvl_cmd == "m" or top_lvl_cmd == "man":
            manual_input()
        elif top_lvl_cmd == "h" or top_lvl_cmd == "help":
            help()
        elif top_lvl_cmd == "q" or top_lvl_cmd == "quit" or top_lvl_cmd == "exit":
            print("Exited\n")
            exit()
        else:
            print('.')


# The help "menu":
def help():
    print('\nWelcome to the help menu\n"'
          'Bot Compose" is a python program designed to "compose" "bots" and automate various tasks\n'
          'Using this tool, the user is able to control the mouse/keyboard in various ways using the\n'
            'mouse/keyboard commands available from the bot model.\n'
            'The most common functions the Model offers include the mouse functions:\n'
        'mv(x, y), clck(btn=l r m), mvclck(x, y, btn),\n as well as keyboard functions:\n'
        'press(btn), hld(btn), rel(btn), wrt(text), and other useful functions like sleep(time), record actions,\n'
        'There are various ways these functions can be composed together to create a sequence of actions to be automated.'
        'reading commands from a file example:\n'
        'sleep 5\nmv 200 120\nsleep 1\nclck l\nclck l\nmvclck 340 215 l\nwrt Hello World!\npress tab\n my name is Jack.\n'
        'The bot also has functions such as rec() for mouse/keyboard events recording, play() for playing recorded events,\n'
        'repeat() for repeating a sequence of events/actions which can be utilized throught read_from_file or manual_input\n'
        'more on them later.'
    )
    print(
        "options:"
        "f, file - read commands from a src .txt file\n"
        "recmouse - start recording mouse events\n"
        "reckb - start recording keyboard events\n"
        "playmouse - replay recorded mouse events\n"
        "playkb - replay recorded keyboard events\n"
        "m, man - enter commands manually(similar to running python intractive terminal)\n"
        "h, help - Display general info about the tool\n"
    )
    print(
        "This tool can be used in numerous ways and the effective usage of it is dependent on the user's imagination.")
    print(
        "The the core concept of this botcomposition/automation program is for it to execute 'commands' set by the user.\n"
    )


if __name__ == "__main__":
    run()
