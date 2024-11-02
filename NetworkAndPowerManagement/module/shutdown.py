import subprocess
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

try:
    minutes = int(input("In how many minutes do you want your system to shutdown? "))
    seconds = minutes * 60
except ValueError:
    print("Enter integers only.")

command = subprocess.run(['shutdown', '/s', '/t', f'{seconds}'])
