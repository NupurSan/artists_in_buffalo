from milestone1 import computeFrequency, filterByKey
from milestone2 import convertToLists, writeRecords, loadRecords, convertToDictionaries


import os
import urllib.request as ur
import csv
import json
import matplotlib.pyplot as plt
import numpy as np

KEYS = ['title','category','type','medium','frame','photo_url_link','artist',
        'site','street_address','city','zip_code','state','latitude','longitude']


def cacheAndLoadData(file):
    if not os.path.isfile(file):
        url = "https://data.buffalony.gov/resource/6xz2-syui.json"
        response = ur.urlopen(url)
        content_string = response.read().decode()
        content = json.loads(content_string)
        to_list = convertToLists(KEYS, content)
        with open(file, "w", newline='') as f1le:
            writer = csv.writer(f1le)
            writer.writerow(KEYS)
            for row in to_list:
                writer.writerow(row)
    records_load = loadRecords(file)
    lod = convertToDictionaries(KEYS, records_load)
    return lod
    

def cleanData(data):
    for value in data:
        if value["category"] == "PAINTINGS":
            value["category"] = "PAINTING"
        elif value["category"] == "DECORATIVE OBJECTS":
            value["category"] = "DECORATIVE OBJECT"
        elif value["category"] == "GRAPHIC":
            value["category"] = "GRAPHIC ARTS"
        elif value["category"] == "GRAPHICS":
            value["category"] = "GRAPHIC ARTS"
        elif value["category"] == "GRAPHICS":
            value["category"] = "GRAPHIC ARTS"
        elif value["category"] == "GRAPHICS ARTS":
            value["category"] = "GRAPHIC ARTS"


def plotPieForKey(key, data):
    occ = computeFrequency(key, data)
    labels = list(occ.keys())
    sizes = list(occ.values())
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Occurence distribution')
    plt.show()

def plotBarForKey(key, data):
    occ = computeFrequency(key, data)
    labels = list(occ.keys())
    values = list(occ.values())

    y_pos = np.arange(len(labels))

    fig, ax = plt.subplots()

    ax.barh(y_pos, values, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  
    ax.set_xlabel('Frequency')
    ax.set_ylabel(key.capitalize())

    plt.show()

def plotFilteredBarForKey(key, fkey, fval, data):
    filtered_data = filterByKey(fkey, fval, data)
    occ = computeFrequency(key, filtered_data)
    labels = list(occ.keys())
    values = list(occ.values())

    y_pos = range(len(labels))

    plt.figure(figsize=(10, 8))
    plt.barh(labels,values)
    plt.xlabel('Frequency')
    plt.show()


