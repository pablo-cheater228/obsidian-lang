import time
prnt = "Something"

lang = input("Select language[Eng=Engish, Rus=Русский]")
if lang == "Eng":
	print("    0000    00000    000000")
	time.sleep(0.5)
	print("   0    0   0   0    0     ")
	time.sleep(0.5)
	print("   0    0   000000   000000")
	time.sleep(0.5)
	print("   0    0   0    0        0")
	time.sleep(0.5)
	print("    0000    000000   000000")
	time.sleep(0.5)
	print("                           ")
	print("Welcome to obsidian client!")
	while True:
		command = input("obs.command>")
		if command == "print":
			prnt = input("What to print:")
			print(prnt)
		if command == "help":
			print("print: Print text.")
			print("help: view this menu")

if lang == "Rus":
	print("    0000    00000    000000")
	time.sleep(0.5)
	print("   0    0   0   0    0     ")
	time.sleep(0.5)
	print("   0    0   000000   000000")
	time.sleep(0.5)
	print("   0    0   0    0        0")
	time.sleep(0.5)
	print("    0000    000000   000000")
	time.sleep(0.5)
	print("                           ")
	print("Добро пожаловать в клиент Obsidian!")
	while True:
		command = input("obs.command>")
		if command == "print":
			prnt = input("Что нужно написать:")
			print(prnt)
		if command == "help":
			print("print: показать текст.")
			print("help: показать это меню.")
