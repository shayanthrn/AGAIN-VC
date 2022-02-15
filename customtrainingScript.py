import subprocess
import sys
import os
from util.parser import get_parser

parser = get_parser(description='deepmine_preprocessor')
parser.add_argument('--path', '-p', default='./', help='wav folder of deepmine dataset')
args = parser.parse_args()
datasetpath = args.path
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


print("installing dependencies...")
packages = ['pyworld','resemblyzer','wandb','librosa','soundfile','requests']
for package in packages:
    try:
        install(package)
    except:
        pass

clearConsole()
print("dependencies installed succesfully!")

current_path = os.getcwd() + "/"

subprocess.check_call([ "python", "deepmine_preprocess.py", "--path", datasetpath])
subprocess.check_call([ "python", "preprocess.py", "-c", "config/preprocess.yaml"])
subprocess.check_call([ "python", "make_indexes.py", "-c", "config/make_indexes.yaml"])
# subprocess.check_call([ "python", "train.py", "-c", "config/train_again-c4s.yaml","--seed","1234567","--total-steps","100000","--save-steps","5000"])