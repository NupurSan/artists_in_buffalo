# Test Case

# convertToDictionaries(["Movie", "Rating"], [["Saw","5"],["It","4"]])
# should return[{"Movie":"Saw", "Rating":"5"},{"Movie":"It", "Rating":"4"}]

def convertToDictionaries(keys,values):
    result = []
    for value_all in values:
        aDict = {}
        for i in range(len(keys)):
            key = keys[i]
            value = value_all[i]
            aDict[key] = value
        result.append(aDict)
    return result
        
import csv

def loadRecords(filename):
    records = []
    count = 0
    with open(filename, newline = '') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if count != 0:
                records.append(row)
            count = count + 1
    return records
# loadRecords("foo.csv")shouldreturn[["Catan", "103"],["Codenames","86"]].

def convertToLists(keys,lod):
    answer = []
    for dictionary in lod:
        results = []
        for key in keys:
            aDict = dictionary.get(key,'')
            results.append(aDict)
        answer.append(results)
    return answer

# Samplefunctioncall: convertToLists(["a","b"],
# [{"a":"foo", "b":"bar"},{"a":"baz"}])shouldreturn [["foo","bar"],["baz",""]].


def writeRecords(filename, records):
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(records)
