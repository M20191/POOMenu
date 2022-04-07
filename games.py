from poomenu import *
menu = Listas()

menu.new_option('Minecraft','echo GOOD GAME!',1)
menu.new_option('CSGO','echo GODDINER GAME!',2)

with keyboard.Listener(menu.run_menu) as listener:
	listener.join()