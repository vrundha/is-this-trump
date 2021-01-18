import sys
import csv
from sklearn.model_selection import train_test_split
import requests
from zipfile import ZipFile
from os import path

dataset = []

if path.exists('Donald Trumps Facebook Statuses  Reaction Counts (as of 10_17_16 minimaxir) - DonaldTrump_facebook_statuses.csv.csv') == False:
    url = "https://www.kaggle.com/jinbonnie/trumps-facbook/download"
    r = requests.get(url, allow_redirects = True)
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

