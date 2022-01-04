import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


print("installing dependencies...")
packages = ['pyworld','resemblyzer','wandb','librosa','soundfile']
for package in packages:
    try:
        install(package)
    except:
        pass
print("dependencies installed succesfully!")