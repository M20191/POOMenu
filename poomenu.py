from pynput import keyboard
import os
import time


# Function
class Listas():

	def __init__(self):
		self.options = {}
		self.menu_index = 0


	#def create_menu(self):
	# RL, UD, Coming Soon
	
	def new_option(self,name,command,pos):
		self.name = name
		self.command = command
		self.pos = pos

		# {1: ["",""] , 2: ["",""]}	
		self.options[pos] = [name,command]


	def new_category(self,cat_name,display_name,pos):
		self.cat_name = cat_name
		self.display_name = display_name
		self.pos = pos

		exute = f"py {cat_name}.py"
		with open(f"{cat_name}.py","w") as ct:
			ct.write("from poomenu import *\nmenu = Listas()\n\n")

		self.options[pos] = [display_name,exute]		

	def new_cat_option(self,name,command,pos,category):
		self.name = name
		self.command = command
		self.pos = pos
		self.category = category

		with open(f"{category}.py","a") as ct:
			option = f"menu.new_option('{name}','{command}',{pos})\n"
			ct.write(option)
	
	def final_cat(self,category):
		self.category = category
		with open(f"{category}.py","a") as ct:
			ct.write("""
with keyboard.Listener(menu.run_menu) as listener:
	listener.join()""")
		




			

	def run_menu(self,key):
		# Exit Program
		if key == keyboard.Key.esc:
			print("Exit program")
			return False


		try:
			if key == keyboard.Key.right:
				self.menu_index += 1

			elif key == keyboard.Key.left:
				self.menu_index -= 1

			elif key == keyboard.Key.enter:
				os.system("cls")
				os.system(f"{self.options[self.menu_index][1]}")
				time.sleep(0.5)
					

			# Display
			os.system("cls")	
			print("Y88-888-888-888-888-888-888-888-888-88Y\n\t",self.options[self.menu_index][0],"\nY88-888-888-888-888-888-888-888-888-88Y")

		except:
			self.menu_index = 0
			print("OUT RANGE, PRESS ENTER TO RETURN")



# Testing

if __name__ == "__main__":
	
	menu = Listas()

	menu.new_option("Option 1","echo Option 1",1)
	menu.new_option("Option 2","echo Option 2",2)
	menu.new_option("Option 3","echo Option 3",3)
	menu.new_option("Option 4","echo Option 4",4)

	menu.new_category("games","Games",5)

	menu.new_cat_option("Minecraft","echo GOOD GAME!",1,"games")
	menu.new_cat_option("CSGO","echo GODDINER GAME!",2,"games")	
	menu.final_cat("games")

	with keyboard.Listener(menu.run_menu) as listener:
		listener.join()










	


