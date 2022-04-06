from pynput import keyboard
import os
from colorama import *

# First interactive model Extract a function from a file
menu_index_option = 0
menu_select_options = {
    1: ["Function 1", "from archive import function","function()"],
    2: ["Function 2", "from archive import function","function()"]
    # More options... ["Name menu, Extract the function from some file and matter this one,import the extracted function"]  
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
            command = menu_select_options[menu_index_option][2]
            with open("command.py","w") as importing:
                writer.write(importing + "\n")
            with open("command.py","a") as append:
                append.write(command)
            
            os.system("python command.py")
        
        elif key == keyboard.Key.esc:
            return False
            # Exit the program
        
        #   
        print(f"Y88-888-888-888-888-888-888-888-888-88Y\n\t\t     ↑\n\n\t\t {menu_select_options[menu_index_option][0]}\n\n\t\t     ↓\nY88-888-888-888-888-888-888-888-888-88Y")
        
    except:
        menu_index_option = 0
        print(f"Y88-888-888-888-888-888-888-888-888-88Y\n\n\t Value out of range \n\nY88-888-888-888-888-888-888-888-888-88Y")

# Key listener
if __name__ == "__main__":
    with keyboard.Listener(key_pressure) as listener:
        listener.join()