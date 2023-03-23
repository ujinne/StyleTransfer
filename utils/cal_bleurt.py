# -*- coding: utf-8 -*-

import sys
from bleurt import score


checkpoint = './checkpoints/bleurt-base-128'
scorer = score.BleurtScorer(checkpoint)

# def cal_bleurt(file0, file1):
#     scores = []
#     with open(file0,'r') as fin:
#         hyps = []
#         for line in fin.readlines():
#             hyps.append(line.strip())
#     for i in range(4):
#         with open(file1+str(i),'r') as fin:
#             refs = []
#             for line in fin.readlines():
#                 refs.append(line.strip())
#             scores.extend(scorer.score(refs, hyps))
#     return scores

def cal_bleurt(file0, file1):
    with open(file0,'r') as fin:
        hyps = []
        for line in fin.readlines():
            hyps.append(line.strip())
    with open(file1,'r') as fin:
        refs = []
        for line in fin.readlines():
            refs.append(line.strip())
    scores = scorer.score(references=refs, candidates=hyps)
    return scores

scores = []
scores.extend(cal_bleurt(sys.argv[1],sys.argv[3]))
scores.extend(cal_bleurt(sys.argv[2],sys.argv[4]))
print('The average bleurt score is {}'.format(sum(scores)/len(scores)))


# checkpoint = '/home/green/Desktop/23_iPactory/pre-trained-formality-transfer/checkpoints/bleurt-base-128'

# # checkpoint = "bleurt/test_checkpoint"
# references = ["This is a test."]
# candidates = ["This is the test."]

# scorer = score.BleurtScorer(checkpoint)
# scores = scorer.score(references=references, candidates=candidates)
# assert isinstance(scores, list) and len(scores) == 1
# print(scores)