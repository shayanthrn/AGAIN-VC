import os
import logging
import numpy as np
import re
from .base import BaseDataset
from util.transform import segment, random_scale
import torch

logger = logging.getLogger(__name__)

class Dataset(BaseDataset):
    def __init__(self, dset, indexes_path, feat, feat_path, seglen, njobs, metadata):
        super().__init__(dset, indexes_path, feat, feat_path, seglen, njobs, metadata)
        self.listofspeakers = os.listdir("./data/wav48")
        self.labelofspeakers = {}
        i = 0
        for speaker in self.listofspeakers:
            temp = torch.zeros(len(self.listofspeakers))
            temp[i] = 1.0
            self.labelofspeakers[speaker[1:]] = temp
            i+=1


    def sub_process(self, each_data, feat, feat_path):
        speaker = each_data[0]
        basename = each_data[1]
        # print(each_data, feat, feat_path)
        ret = {}
        for f in feat:
            path = os.path.join(feat_path, f, basename)
            if os.path.isfile(path):
                ret[f] = np.load(path)
            else:
                logger.info(f'Skip {path} {f}: invalid file.')
                return
        ret['speaker'] = speaker
        return ret
    
    def __getitem__(self, index):
        speaker = self.data[index]['speaker']
        mel = self.data[index]['mel']
        mel = segment(mel, return_r=False, seglen=self.seglen)

        meta = {
            'mel': mel,
            'speaker': speaker,
            'label': self.labelofspeakers[speaker]
        }
        return meta