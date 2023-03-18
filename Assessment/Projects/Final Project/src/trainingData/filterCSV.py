# read CSV file and filter out the data that is not matched with the file name in the folder

import csv
import os

# read the file name in the folder
def readFileName():
    fileNames = []
    for root, dirs, files in os.walk("/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/test_3/training_filtered"):
        for file in files:
            # if the file is png file
            if file.endswith(".png"):
                name1 = file.split('_')[1]
                # remove the extension
                name2 = name1.split('.')
                name3 = "{}.{}".format(name2[0], name2[1])
                fileNames.append(name3)
    return fileNames

# read the csv file
def readCSV():
    fileNames = readFileName()
    with open('/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/test_3/trainingData.csv', 'r') as f:
        reader = csv.reader(f)
        # skip the header
        next(reader)
        for row in reader:
            if row[0] in fileNames:
                # write the data to the new csv file
                with open('/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/test_3/trainingData_filtered.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(row)

readCSV()