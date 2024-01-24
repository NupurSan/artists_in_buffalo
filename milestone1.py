# Test cases
# getValuesforKey("Artist", data) => ['UNKNOWN', 'SMITHBROTHERSCOMPANY', 'NATHANNAETZKER', 'ALVAHBRADISH']

def getValuesForKey(key, records):
    acc = []
    for rec in records:
        if key in rec:
            value = rec[key]
            # Check if the value is not already in 'acc'
            if value not in acc:
                # If not, append the value to 'acc'
                acc.append(value)
    return acc

# Test Cases
# countMatchesByKey("Artist", "BIFF HENRICH", data) => 0
# countMatchesByKey("Category", "SCULPTURE", data) => 1

def countMatchesByKey(key,value,records):
    count = 0
    for rec in records:
        if key in rec and rec[key] == value:
            # goes over the record to see if 'key' exists and if that 'key'
            # matches th given vale 
            count = count + 1
    return count

# Test Cases
# countMatchesByKeys("Artist", "JOSHUA G STEIN", "Category", "SCULPTURE", data)=>0 => 0
# countMatchesByKeys('Category', 'SCULPTURE', 'Artist', 'UNKNOWN', data) => 1

def countMatchesByKeys(key1,value1,key2,value2,records):
    count = 0
    for rec in records:
        if key1 in rec and rec[key1] == value1:
            if key2 in rec and rec[key2] == value2:
                # same as above but now we are looking at more than 1 key
                count = count + 1
    return count

# Test Cases
# filterByKey("Category", "SCULPTURE", data) =>
# [{'Title': 'SOLEPARK', 'Category': 'SCULPTURE', 'Type': 'RELIEF',
# 'Medium': 'STONE', 'Frame': 'false', 'PhotoURLLink': 'UNKNOWN',
# 'Artist': 'UNKNOWN', 'StreetAddress': 'BUSTIAVE&NIAGARAST',
# 'City': 'BUFFALO', 'Zipcode': '14213', 'State': 'NY'}]

def filterByKey(key,value,records):
    acc = []
    for rec in records:
        if key in rec and rec[key] == value:
            # if key exists in record and if that matches value
            # same as above concept but we're not interested in count but actual
            # values
            acc.append(rec)
    return acc
        
# Test Cases
# computeFrequency("Category", data) =>
# {'SCULPTURE': 1, 'GRAPHICARTS': 2, 'PAINTINGS': 3, 'GRAPHICSARTS': 1}

def computeFrequency(key,records):
    acc = {}
    for rec in records:
        if key in rec:
            # if key exists in current dict
            value = rec[key]
            # if key exists, get its associated value
            if value in acc:
                # checks value is already in acc dict
                acc[value] = acc[value] + 1
            else:
                # if not, add it as a key with a count of 1
                acc[value] = 1
    return acc
