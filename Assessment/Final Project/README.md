
# AI-Powered Indoor Locator


An AI-powered indoor positioning system that helps visitors navigate complex buildings.

  

## The latest training model

>https://github.com/Lionel-Lim/casa0018/blob/main/Assessment/Final%20Project/src/trainingData/test_6/test6.ipynb

  

## Problem Definition

  

### Project Overview

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/marshgateCrosssection.jpeg" width="600" alt="Cross section of Marshgate">  <br>  <em>Figure 1. Cross section of Marshgate (AKT II, 2022)</em>  </p>

**Navigating** large, complex buildings like the newly constructed Marsh Gate at UCL East (Figure 1) can be challenging for newcomers. **Traditional GPS signals are limited indoors** due to structural barriers, making it difficult to pinpoint a user's location. This project aims to **address this issue by utilising a smart camera with built-in AI capabilities** to identify users' locations within the building.


### Research Question

### *Is it possible for an AI-powered smart camera to accurately determine a user's indoor location using depth imagery?*


### Data Available

I collected five training sets in the CE Lab, each containing around 3,000 images. The data collection process involved gathering depth images, orientation, and acceleration data along with the position of the user.

  
  

## Experiments and Results


### Model Training Results

Various trainings were conducted to fine-tune the model, adjusting parameters such as learning rate, epochs, batch size and IMU data. As shown in Figure 2 and 3 below, I found almost identical performance when using depth and IMU data together and when using depth images alone. Therefore, **only depth images is used for the best performance while spending fewer resources.**

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/trainingResult_DepthImageAndImu.png" width="800" alt="Training result using depth image and imu data">  <br>  <em>Figure 2. Training result using depth image and imu data (Accuracy - 0.9781)</em>  </p>
<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/trainingResult_onlyDepthImage.png" width="800" alt="Training result using only depth image">  <br>  <em>Figure 3. Training result using only depth image (Accuracy - 0.9777)</em>  </p>

### Limitation
In the initial stages of the project, the AI model was designed to predict the XYZ coordinates of a user within the indoor environment. However, due to a combination of insufficient data and the dynamic environment, the AI model's accuracy was compromised. As a result, the model's prediction capabilities were adjusted to identify a grid zone where the user is located, instead of the exact coordinates.

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/Visualisation_Blender.png" width="800" alt="Grid zoning with the captured data">  <br>  <em>Figure 4. Grid zoning with the captured data.</em>  </p>

Therefore, the Connected Environments Lab (CE Lab) was **divided into 28 distinct grid zones**. Figure 4 shows the XY coordinates of the captured data indexed by zone and visualised in different colours depending on the zone. The data is the result of starting and ending the measurement at the Telephone Box, i.e. 0,0 relative coordinates. This approach **allowed for the distribution of the training data into equal volumes** for each grid zone. By doing so, the AI model's **performance was optimised given the available data and environmental challenges**.

Despite the limitations in predicting XYZ coordinates, the AI model's grid zone predictions still provide valuable information for users navigating the indoor environment. Further improvements and data collection can potentially enhance the model's accuracy and revert back to the initial goal of predicting precise coordinates in the future.

### Model Architecture Choices

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/AIarchitectures.png" width="500" alt="Trainined Model Architecture">  <br>  <em>Figure 5. Trainined Model Architecture.</em>  </p>

The TensorFlow model (Figure 5) is a Convolutional Neural Network (CNN) designed for processing depth map images to predict a user's indoor location within a grid. The purpose of using a CNN is to learn spatial features and patterns from the input images, making it an ideal choice for handling depth maps.

The first layer is **a convolutional layer** with 16 filters of size 3x3. This layer helps to capture local features from the input image. After this layer, **batch normalization** is applied to stabilize and accelerate training (De and Smith, 2020), followed by **a ReLU activation function** that introduces non-linearity and helps the network learn complex patterns (Chang and Chen, 2015). 

The second layer is a **max-pooling layer** with a pool size of 2x2, which reduces the spatial dimensions of the input, leading to a more compact representation and faster computation.

The model continues with **three more convolutional layers, each followed by a max-pooling layer**. These layers (with 32, 64, and 128 filters respectively) allow the model to learn higher-level features by capturing progressively larger spatial patterns in the depth map.

The **flattened output** is passed through a fully connected (dense) layer with 256 neurons and **a ReLU activation function**, which helps the network learn complex, high-level abstractions from the extracted features (Chang and Chen, 2015).

**A dropout layer** with a rate of 0.5 is added to prevent overfitting by randomly setting a fraction of the input units to zero during training (TensorFlow, 2023).

The final output layer is **a dense layer with 28 neurons and a softmax activation function,** which produces a probability distribution over the 28 grid cells representing the user's location. The softmax activation ensures that the sum of probabilities across all grid cells is equal to 1, making it suitable for multi-class classification tasks.

### Visual Record of Experiments

The AI model's performance was assessed by visualising the predicted grid zones against the actual data points. This allowed us to better understand the model's ability to accurately locate users within the building.

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/Visulisation_ResultMatrix.png" width="500" alt="Prediction of the trained model">  <br>  <em>Figure 6. Prediction of the trained model.</em>  </p>


## Application

### Application Architecture

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/ApplicationArchitectures.png" width="600" alt="Application architecture">  <br>  <em>Figure 7. Application architecture.</em>  </p>

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

The current AI model has some weaknesses, including its reliance on a single smart camera and the limited amount of data collected. Additionally, the model's performance is affected by changes in the environment and the quality of the data collected.


## Bibliography

_If you added any references then add them in here using this format:_

1.  Last name, First initial. (Year published). Title. Edition. (Only include the edition if it is not the first edition) City published: Publisher, Page(s).  [http://google.com](http://google.com/)
    
2.  Last name, First initial. (Year published). Title. Edition. (Only include the edition if it is not the first edition) City published: Publisher, Page(s).  [http://google.com](http://google.com/)
    

_Tip: we use  [https://www.citethisforme.com](https://www.citethisforme.com/)  to make this task even easier._

----------

## Declaration of Authorship

I, Dongyoung Lim, confirm that the work presented in this assessment is my own. Where information has been derived from other sources, I confirm that this has been indicated in the work.

Dongyoung Lim

23 Apr 2023