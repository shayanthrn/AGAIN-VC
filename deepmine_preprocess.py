from util.parser import get_parser
import random

parser = get_parser(description='deepmine_preprocessor')
parser.add_argument('--path', '-p', default='./', help='wav folder of deepmine dataset')

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

#choose 20 sample from females max = 27
females= random.sample([a for a in speakers_list if a['gender'] == 'female'],20)

#choose 20 sample from males  max = 38
males = random.sample([a for a in speakers_list if a['gender'] == 'male'],30)
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

print(final_listofdataset)
