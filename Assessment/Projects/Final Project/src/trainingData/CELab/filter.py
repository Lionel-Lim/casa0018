import cv2
import numpy as np
import os

input_folder = "/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/CELab/ce/"
output_folder = "/Users/dylim/Documents/CASA/CE/casa0018/Assessment/Projects/Final Project/src/trainingData/CELab/filtered/"

# Loop over all files in the input folder
for file_name in os.listdir(input_folder):
    print(file_name)
    input_path = os.path.join(input_folder, file_name)

    # Load the depth image
    depth_img = cv2.imread(input_path)

    # Convert the depth image to grayscale
    depth_gray = cv2.cvtColor(depth_img, cv2.COLOR_BGR2GRAY)

    # Apply a bilateral filter to preserve edges while smoothing
    bilateral_filtered = cv2.bilateralFilter(depth_gray, d=9, sigmaColor=75, sigmaSpace=75)

    # Apply a median filter to reduce noise further
    median_filtered = cv2.medianBlur(bilateral_filtered, ksize=5)

    # Fill in any missing values using inpainting
    # Create a mask for missing values (assuming 0 is a missing value)
    mask = cv2.inRange(median_filtered, 0, 0)

    # Apply inpainting using the mask and a radius of 3
    inpaint_radius = 3
    inpainted = cv2.inpaint(median_filtered, mask, inpaint_radius, cv2.INPAINT_NS)

    output_path = os.path.join(output_folder, file_name)

    # Save the filtered depth image
    cv2.imwrite(output_path, inpainted)
