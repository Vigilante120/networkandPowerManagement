import subprocess
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
# OPTION_4
command = subprocess.run(['shutdown', '-a'])
print(f"{GREEN}SHUTDOWN/RESTART ABORTED!\n{RESET}")