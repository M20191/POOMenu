from pynput import keyboard
import os
import time
from colorama import *


# First interactive model Extract a function from a file
menu_index_option = 0
menu_select_options = {
    1: ["Function 1", "echo Nais! :D"],
    2: ["Function 2", "echo Hello!"]

    # More options... ["Display name, command on CMD"]
    # The command can be both linux and windows, it depends on what you want to run  
}


def key_pressure(key):
    try:
        global menu_index_option
        global menu_select_options
        os.system("cls")

        if key == keyboard.Key.up:
            menu_index_option += 1
                
        elif key == keyboard.Key.down:
            menu_index_option -= 1
        
        elif key == keyboard.Key.enter:
            importing = menu_select_options[menu_index_option][1]
            os.system(f"{importing}")
            time.sleep(5)
            os.system("cls")
            
        elif key == keyboard.Key.esc:
            return False
            # Exit the program

        print(f"Y88-888-888-888-888-888-888-888-888-88Y\n\t\t     ↑\n\n\t\t {menu_select_options[menu_index_option][0]}\n\n\t\t     ↓\nY88-888-888-888-888-888-888-888-888-88Y")
        
    except:
        menu_index_option = 1
        print(f"Y88-888-888-888-888-888-888-888-888-88Y\n\n\t Value out of range \n\t\tESC FOR EXIT\nY88-888-888-888-888-888-888-888-888-88Y")

# Key listener
if __name__ == "__main__":
    with keyboard.Listener(key_pressure) as listener:
        listener.join()