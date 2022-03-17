from pynput import keyboard
import os
import time
from colorama import *
init()

# First interactive model Extract a function from a file
menu_index_option = 2
menu_select_options = {
    1: ["Option 1", "echo Option 1",],
    2: ["Option 2", "echo Option 2",],
    3: ["Option 3", "echo Option 3"],
    4: ["",""]
    # More options... ["Display name, command on CMD"]
    # The command can be both linux and windows, it depends on what you want to run  
}


def key_pressure(key):
    try:
        global menu_index_option
        global menu_select_options
        os.system("cls")

        if key == keyboard.Key.right:
            menu_index_option += 1
                
        elif key == keyboard.Key.left:
            menu_index_option -= 1
        
        elif key == keyboard.Key.enter:
            importing = menu_select_options[menu_index_option][1]
            os.system(f"{importing}")
            time.sleep(5)
            os.system("cls")
            
        elif key == keyboard.Key.esc:
            return False
            # Exit the program
        
        # Second and first display
        menu_index_option_second = menu_index_option + 1
        second = menu_select_options[menu_index_option_second][0]
        menu_index_option_first = menu_index_option - 1
        first = menu_select_options[menu_index_option_first][0]

        print(
            f"""
            Y88-888-888-888-888-888-888-888-888-88Y
            
         {first} <<<  \033[1m \033[92m {menu_select_options[menu_index_option][0]} \033[92m \033[0m {Fore.WHITE}  >>>  {second}   
            
            Y88-888-888-888-888-888-888-888-888-88Y

             """)
        
    except:
        menu_index_option = 1
        menu_index_option_second = menu_index_option + 1
        second = menu_select_options[menu_index_option_second][0]

        print(
            f"""
            Y88-888-888-888-888-888-888-888-888-88Y
            
            \t\t<<< {Fore.WHITE} \033[92m {menu_select_options[menu_index_option][0]} \033[92m {Fore.WHITE} >>> {second}  
            
            Y88-888-888-888-888-888-888-888-888-88Y

             """)


# Key listener
if __name__ == "__main__":
    with keyboard.Listener(key_pressure) as listener:
        listener.join()