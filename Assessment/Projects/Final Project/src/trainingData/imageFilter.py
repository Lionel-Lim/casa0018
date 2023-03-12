import cv2
import os

input_folder = "./result/"
output_folder = "./filtered/"

# Loop over all files in the input folder
for file_name in os.listdir(input_folder):
    print(file_name)
    input_path = os.path.join(input_folder, file_name)

    # Load the depth image
    depth_img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply median filter
    median_img = cv2.medianBlur(depth_img, 5)

    # Apply bilateral filter
    bilateral_img = cv2.bilateralFilter(median_img, 9, 50, 50)

    # Create output path for saving the converted image
    output_path = os.path.join(output_folder, file_name)

    # Save the output image
    cv2.imwrite(output_path, bilateral_img)
