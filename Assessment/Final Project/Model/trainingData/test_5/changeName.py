import os

# specify the directory where the files are located
directory = '/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/test_6/depth_filtered/'

# loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.png'):
        # split the file name into a list based on the '_' character
        parts = filename.split('_')
        # remove the first element of the list (the prefix)
        new_name = '_'.join(parts[1:])
        # rename the file with the new name
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
