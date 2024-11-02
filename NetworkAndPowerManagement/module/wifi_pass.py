import subprocess
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{}{:<30}|  {:<}{}".format(GREEN, i, results[0], RESET))
    except IndexError and subprocess.CalledProcessError:
        print("{}{:<30}|  {:<}{}".format(RED, i, "", RESET))

print(f"{RED}[!]IF ANY ERROR OCCURED MAKE SURE THE WIFI-NAMES ARE IN ASCII FORMAT (A-Z) and (0-9) any thing else will return in error{RESET}\n")
