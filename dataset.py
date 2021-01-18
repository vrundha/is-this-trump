import sys
import csv
from sklearn.model_selection import train_test_split
import requests
from zipfile import ZipFile
from os import path

dataset = []

if path.exists('Donald Trumps Facebook Statuses  Reaction Counts (as of 10_17_16 minimaxir) - DonaldTrump_facebook_statuses.csv.csv') == False:
    url = "https://storage.googleapis.com/kaggle-data-sets/959201/1627649/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210118%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210118T023137Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=47025c30a9c1346ef022e9cc36b5f0f1cf3155d5b817cbe08e97a0cd33bf79de42ca40e724be807aef77d1b0f3f3ee6022ab6f9cbef9fc114bd2471761561b716ce85515cd017bb6d03e56ce0df8a7336b78cb7ff2608782f331b6e1ea1e8a5ac98723784b76329a0dfe9cb7273f85de219aaad3d2dca2c507921d3fa11c7ba3f54c6b700714037bc85fb00cd02c0f1abe588783c9513edbe505377ffdd6840df5da15e88e35e878a74b057ba0dd936da329978003f6198354da0985175bfa6ae4fa62826fbdfb046fd0d814fd92b491e964c1cb5841f2d4d55b18e3d065871b53b4531bec5cd5665d293350b0db139f54cc1e39feac78d8a19e94effe925f2c"
    r = requests.get(url, allow_redirects = True)
    open('archive.zip','wb').write(r.content)
    with ZipFile('archive.zip','r') as zipObj:
        zipObj.extractall()
else:
    print("File containing the dataset already present")

with open('Donald Trumps Facebook Statuses  Reaction Counts (as of 10_17_16 minimaxir) - DonaldTrump_facebook_statuses.csv.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        dataset.append("<|title|>" + row[1] + "<|endoftext|>")
train_set, validation_set = train_test_split(dataset, train_size=0.9)

if path.exists(sys.argv[1]) == True or path.exists(sys.argv[2]) == True:
    print("File specified already exists and will be overwritten")

with open(sys.argv[1], 'w') as f:
    f.write("".join(train_set))
with open(sys.argv[2], 'w') as f:
    f.write("".join(validation_set))

