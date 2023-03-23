import os

sentiment = [0, 1]
for sent in sentiment:
    if sent == 0:
        tgt_sent = 1
    else:
        tgt_sent = 0
    datapath=f'/home/green/Desktop/23_iPactory/DualRL/data/yelp/tsf_template/train.{sent}-{tgt_sent}.tsf'
    savepath = 'data/yelp/'
    os.makedirs(savepath, exist_ok=True)
    with open(datapath, 'r') as data:
        texts = data.readlines()
        len_train = int(len(texts)*0.8)
        with open(f'{savepath}/train.{sent}', 'w') as file:
            file.writelines(i.split('\t')[0].strip()+'\n' for i in texts[:len_train])
        with open(f'{savepath}/train_pseudo.{sent}', 'w') as file:
            file.writelines(i.split('\t')[1].strip()+'\n' for i in texts[:len_train])
        with open(f'{savepath}/valid.{sent}', 'w') as file:
            file.writelines(i.split('\t')[0].strip()+'\n' for i in texts[len_train:])
        with open(f'{savepath}/valid_pseudo.{sent}', 'w') as file:
            file.writelines(i.split('\t')[1].strip()+'\n' for i in texts[len_train:])

datapath='/home/green/Desktop/23_iPactory/DualRL/data/yelp/'
savepath = 'data/yelp/'
os.makedirs(savepath, exist_ok=True)
for sent in sentiment:
    with open(f'{datapath}/test.{sent}', 'r') as data:
        texts = data.readlines()
        with open(f'{savepath}/test.{sent}', 'w') as file:
            file.writelines(i.strip()+'\n' for i in texts[:100])

