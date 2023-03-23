# AI- Powered Indoor Locator

An AI-powered indoor positioning system to help new students and staff navigate the Marsh Gate building at UCL East.

## The latest training model
>https://github.com/Lionel-Lim/casa0018/blob/main/Assessment/Projects/Final%20Project/src/trainingData/test_6/test6.ipynb

## Problem Definition

### Project Overview
Navigating large, complex buildings like the newly constructed Marsh Gate at UCL East can be challenging for newcomers. Traditional GPS signals are limited indoors due to structural barriers, making it difficult to pinpoint a user's location. This project aims to address this issue by utilizing a smart camera with built-in AI capabilities to identify users' locations within the building.

### Research Question
>Can we accurately determine a user's indoor location using a combination of depth images, orientation, and acceleration data collected from an AI-powered smart camera?

![Collected Data shown on Blender](https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Report/src/Visualisation_Blender.png)

### Data Available
I collected five training sets in the CE Lab, each containing around 3,000 images. The data collection process involved gathering depth images, orientation, and acceleration data along with the position of the user.


## Documentation of Experiments and Results

![Tensorflow Model Layer Structure](https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Report/src/Visualisation_AIModel.png)

### Model Training Results
Various training runs were conducted to fine-tune the model, adjusting parameters such as learning rate, epochs, and batch size. I achieved the best performance using a combination of depth and IMU data.

### Model Architecture Choices
The model processes depth information through CNN layers and IMU data through dense layers. Dropout layers are used to prevent overfitting. However, the role of IMU data is weak.

![Training Result in matrix form](https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Report/src/Visulisation_ResultMatrix.png)

### Visual Record of Experiments
The AI model's performance was assessed by visualising the predicted grid zones against the actual data points. This allowed us to better understand the model's ability to accurately locate users within the building.

## Critical Reflection and Learning from Experiments

### Observations from Experiments
The AI model was not entirely accurate in predicting the user's location. However, it was able to provide approximate locations in most cases. It performed better in predicting grid zones with a larger amount of data.

### Factors Influencing Results
Several factors influenced the results, including:

1. Dynamic Target Environment: The CE Lab's constantly changing layout made it difficult to collect consistent data.
2. Limitations of the Depth Camera and IMU: The relative coordinates obtained by the Oak-D camera contained noise, which negatively impacted the training process.
3. Data Collection and Processing Time: Setting up the depth camera and processing the data took a significant amount of time.
4. Limited Resources: Training the AI model required considerable resources, and the resources provided by Google Colab were insufficient.

### Potential Improvements
To improve the model's performance, the following steps can be considered:

1. Collect more data to better train the AI model, especially in underrepresented grid zones.
2. Enhance the data processing pipeline to better filter noise and improve data quality.
3. Optimize the AI model's architecture to reduce overfitting and improve generalization.
4. Utilize more powerful computing resources to enable faster training and experimentation.

### Weaknesses
The current AI model has some weaknesses, including its reliance on a single smart camera and the limited amount of data collected. Additionally, the model's performance is affected by changes in the environment and the quality of the data collected.