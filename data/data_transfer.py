# -*- coding: utf-8 -*-
import os, re, json, traceback

# train.json -> clinical.train,
# test.json -> clinical.test
# dev.json -> clinical.dev
with open("./json_data/test.json", "r", encoding="utf-8") as f:
    content = [_.strip() for _ in f.readlines()]

f = open("./data/clinical.test", "w", encoding="utf-8")

#for line in content:
#    sample = json.loads(line)
#    text = sample["text"]
#    tags = ['O'] * len(text)
#    for label, label_dict in sample["label"].items():
#        for key, val in label_dict.items():
#            if val == []:
#                continue
#            start_index = val[0][0]
#            tags[start_index] = 'B-%s' % label
#            end_index = val[0][1]
#            for i in range(start_index+1, end_index+1):
#                tags[i] = 'I-%s' % label
#
#    for char, tag in zip(text, tags):
#        f.write(char+' '+tag+'\n')
#
#    f.write('\n')
for sample in content:
    line = json.loads(sample)
    text = line["text"]
    tags = ['O'] * len(text)
    for label, label_dict in line["label"].items():
        for key, vals in label_dict.items():
            if vals == []:
                continue
            #print(vals)
            for val in vals:
                start_index = val[0]
                tags[start_index] = 'B-%s' % label
                end_index = val[1]
                for i in range(start_index+1, end_index):
                    tags[i] = 'I-%s' % label
    for char, tag in zip(text, tags):
        f.write(char+' '+tag+'\n')
    
    f.write('\n')