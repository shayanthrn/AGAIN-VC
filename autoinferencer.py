import subprocess
import sys
import os
expname = "withoutspeakerverification"
waves = ["../testwaves/female_4sec_intrainset.wav","../testwaves/female_20sec_intrainset.wav","../testwaves/male_4sec_intrainset.wav","../testwaves/male_7sec_intrainset.wav","../testwaves/outofset_male_7sec.wav"]
checkpointpath = "../NormalLR_cpk_15eachspeaker/steps_100000.pth"
for source in waves:
    for target in waves:
        #python inference.py -c config/train_again-c4s.yaml -l ../NormalLR_cpk_15eachspeaker/steps_100000.pth -s ../testwaves/female_4sec_intrainset.wav -t ../testwaves/female_4sec_intrainset.wav -o data/newvocoder
        subprocess.check_call([ "python", "inference.py", "-c", "config/train_again-c4s.yaml","-l",checkpointpath,"-s",source,"-t",target,"-o",f"data/{expname}"])