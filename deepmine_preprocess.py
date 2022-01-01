from util.parser import get_parser
import random
import os
import librosa
import soundfile as sf



def convert_to_second(x):
    splited = x.split(':')
    min_to_sec = float(splited[1])*60
    sec = float(splited[2])
    return min_to_sec+sec


parser = get_parser(description='deepmine_preprocessor')
parser.add_argument('--path', '-p', default='./', help='wav folder of deepmine dataset')
args = parser.parse_args()
if(args.path[-1]!="/"):
    args.path+="/"

speakerlist = open("speakers.lst","r")
speakers  = speakerlist.readlines()
speakers_list = []
for speaker in speakers:
    data = speaker.split(' ')
    if('male' in data):
        gender = 'male'
    elif('female' in data):
        gender = 'female'
    else:
        gender = "unkown"
    if(gender != "unkown"):
        object = {'id':data[0],'gender':gender}
        speakers_list.append(object)

#choose 20 sample from females max = 27 (20 train 7 test)
females= random.sample([a for a in speakers_list if a['gender'] == 'female'],27) 

#choose 20 sample from males  max = 38 (30 train 8 test)
males = random.sample([a for a in speakers_list if a['gender'] == 'male'],38)
finalspeakers = males+females


file2speaker = open('file2speaker.lst','r')
file2speake_list = file2speaker.read().splitlines()[1:]
files_list = []
for file in file2speake_list:
    data = file.split(' ')
    object = {'file_id':data[0],'speaker_id':data[1]}
    files_list.append(object)

final_listofdataset = []


#min file from speaker = 6

for speaker in finalspeakers:
    spkid = speaker['id']
    final_listofdataset+= random.sample([a for a in files_list if a['speaker_id'] == spkid],6)


transcripts = open('all_segments.lst')
transcripts = transcripts.readlines()
transcripts = transcripts[1:]
segments = {}
for i in transcripts:
    splited = i.split(' ')
    fileid = splited[2]
    start =convert_to_second(splited[4]) 
    end = convert_to_second(splited[6]) 
    start_end = (start,end)
    if(fileid in segments.keys()):
        segments[fileid].append(start_end)
    else:
        segments[fileid] = [start_end]


datasetpath = args.path
for file in final_listofdataset:
    file_path = datasetpath + file['file_id'] + ".wav"
    path = "./data/wav48/" + "p" +file['speaker_id'] + "/"
    if(os.path.exists(path)):
        pass
    else:
        os.makedirs(path)
    audio, sr = librosa.load(file_path,mono=True)
    file_segments = segments[file['file_id']]
    idcounter = 0
    for segment in file_segments:
        outputname = path + file['speaker_id'] + "_" + str(idcounter)
        start = segment[0] * sr
        end = segment[1] * sr
        data = audio[int(start):int(end)]
        sf.write(outputname, data, sr)
        idcounter+=1
    
    
