import subprocess
import sys
import os


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# print("installing dependencies...")
# packages = ['pyworld','resemblyzer','wandb','librosa','soundfile','requests']
# for package in packages:
#     try:
#         install(package)
#     except:
#         pass

# clearConsole()
# print("dependencies installed succesfully!")

current_path = os.getcwd() + "/"