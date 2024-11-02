import os
import subprocess
BLUE = '\033[94m'
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
CYAN = '\033[96m'


print(f"{BLUE}Welcome to Tricks of CMD{RESET}")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


options = [
    f"{CYAN}\n1. Show Wifi Password",
    "2. Restart the system\n"
    "3. Shutdown the system\n"
    "4. Abort The shutdown or restart process",
    # '5. \n'
    f"0. To Exit{RESET}"

]


def handle_selection(selection):
    try:
        selection = int(selection)
        if selection == 1:
            clear_screen()
            print(f"{GREEN}Displaying Password of all your connected wifi network{RESET}")
            wifi_pass = "python module/wifi_pass.py"
            subprocess.run(wifi_pass, shell=True)

        elif selection == 2:
            clear_screen()
            print(f"{RED} Restarting the system.{RESET}")
            restart = "python module/restart.py"
            subprocess.run(restart, shell=True)

        elif selection == 3:
            clear_screen()
            print(f"{RED}ShutDown Option Selected.{RESET}")
            shutdown = "python module/shutdown.py"
            subprocess.run(shutdown, shell=True)

        elif selection == 4:
            clear_screen()
            print(f"{GREEN}ABORTING THE PROCESS.{RESET}")
            abort = "python module/abort.py"
            subprocess.run(abort, shell=True)

        elif selection == 0:
            print(f"{RED}EXITING..{RESET}")
            exit()
        else:
            print("[-] Invalid Selection")
    except ValueError:
        print("[-] Please enter a valid number.")


def main():
    while True:
        clear_screen()
        print("\n".join(options))
        choice = input(f"{GREEN}Select an Option (0-4): {RESET}").strip()
        if choice == '0':
            print("Exiting the program.")
            break
        handle_selection(choice)


if __name__ == "__main__":
    main()