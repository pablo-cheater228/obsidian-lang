import time
import sys
prnt = "Something"

lang = input("Select language[eng=Engish, rus=Русский]")
if lang == "eng":
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
			print("exit: Exit program.")
			print("version: view lang version.")
			print("help: view this menu")
		if command == "exit":
			sys.exit()
		if command == "ver" or "version":
			print("OBSIDIAN_LANG. v1.0alpha-beta ENG")

if lang == "rus":
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
			print("ver: отобразить версию языка.")
			print("exit: закрыть программу.")
			print("help: показать это меню.")
		if command == "exit":
			sys.exit()
		if command == "ver" or "version":
			print("OBSIDIAN_LANG. v1.0alpha-beta RUS")
