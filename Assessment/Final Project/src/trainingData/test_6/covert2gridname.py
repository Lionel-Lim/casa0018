import os
import csv

# Set the path to the folder containing the files to rename
folder_path = "/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/test_6/depth_filtered copy"

# Set the path to the CSV file
csv_path = "/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/test_6/filtered_grid.csv"

# Read the CSV file into a dictionary
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    # Create a dictionary of filename and new name pairs
    file_dict = {f"{row[0]}.png": row[5] for row in csv_reader}

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the filename matches a value in the CSV file's second column
    if filename in file_dict:
        # Get the new filename from the corresponding value in the CSV file's fifth column
        new_filename = file_dict[filename]
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
