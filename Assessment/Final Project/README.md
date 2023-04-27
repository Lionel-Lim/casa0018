
# AI-Powered Indoor Locator


An AI-powered indoor positioning system that helps visitors navigate complex buildings.

  

## The latest training model

>https://github.com/Lionel-Lim/casa0018/blob/main/Assessment/Final%20Project/src/trainingData/test_6/test6.ipynb

  

## Problem Definition

  

### Project Overview

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/marshgateCrosssection.jpeg" width="500" alt="Cross section of Marshgate">  <br>  <em>Figure 1. Cross section of Marshgate (AKT II, 2022)</em>  </p>

**Navigating** large, complex buildings like the newly constructed Marsh Gate at UCL East (Figure 1) can be challenging for newcomers. **Traditional GPS signals are limited indoors** due to structural barriers, making it difficult to pinpoint a user's location. This project aims to **address this issue by utilising a smart camera with built-in AI capabilities** to identify users' locations within the building.


### Research Question

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/lostperson.jpg" width="500" alt="Lost person in a complex building"> <br> <em>(Microsoft, 2022)</em>   </p>

### *Is it possible for an AI-powered smart camera to accurately determine a user's indoor location using depth imagery?*

## Oak-D Camera

<p align="center">  <img src="https://cdn.shopify.com/s/files/1/0106/8325/2802/products/Asset5-100_a23479fc-7d0c-4058-913a-966243a078ab.jpg?v=1679660052" width="500" alt="Oak-D Camera">  <br>  <em>Figure 2. Oak-D Camera (Luxonis, 2021).</em>  </p>

The Oak-D camera (Figure 2) is an AI-powered smart camera developed by Luxonis that integrates a powerful depth sensor, a neural processing unit, and a standard RGB camera. It is designed for various computer vision and AI applications, including object tracking, and gesture recognition (OpenCV and Luxonis, 2021).

The primary advantage of using the Oak-D camera is its ability to deploy AI models directly on the camera. This has several benefits:

- Edge processing: By running the AI model directly on the camera, AI model can be performed at the edge, which means the data processing happens locally on the device. This reduces latency, as it doesn't need to send the data to a remote server for processing.

- Privacy: Since the data is processed on the camera itself, sensitive information does not need to be transmitted over the internet, which can help maintain user privacy.

- Bandwidth and network efficiency: Processing data on the camera reduces the amount of data that needs to be transmitted over the network, saving bandwidth and decreasing the load on the network infrastructure.

  
## Experiments and Results


### Model Training Results

Various trainings were conducted to fine-tune the model, adjusting parameters such as learning rate, epochs, batch size and IMU data. As shown in Figure 3 and 4 below, I found almost identical performance when using depth and IMU data together and when using depth images alone. Therefore, **only depth images is used for the best performance while spending fewer resources.**

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/trainingResult_DepthImageAndImu.png" width="800" alt="Training result using depth image and imu data">  <br>  <em>Figure 3. Training result using depth image and imu data (Accuracy - 0.9781)</em>  </p>
<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/trainingResult_onlyDepthImage.png" width="800" alt="Training result using only depth image">  <br>  <em>Figure 4. Training result using only depth image (Accuracy - 0.9777)</em>  </p>

### Limitation
In the initial stages of the project, the AI model was designed to predict the XYZ coordinates of a user within the indoor environment. However, due to a combination of insufficient data and the dynamic environment, the AI model's accuracy was compromised. As a result, the model's prediction capabilities were adjusted to identify a grid zone where the user is located, instead of the exact coordinates.

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/Visualisation_Blender.png" width="800" alt="Grid zoning with the captured data">  <br>  <em>Figure 5. Grid zoning with the captured data.</em>  </p>

Therefore, the Connected Environments Lab (CE Lab) was **divided into 28 distinct grid zones**. Figure 5 shows the XY coordinates of the captured data indexed by zone and visualised in different colours depending on the zone. The data is the result of starting and ending the measurement at the Telephone Box, i.e. 0,0 relative coordinates. This approach **allowed for the distribution of the training data into equal volumes** for each grid zone. By doing so, the AI model's **performance was optimised given the available data and environmental challenges**.

Despite the limitations in predicting XYZ coordinates, the AI model's grid zone predictions still provide valuable information for users navigating the indoor environment. Further improvements and data collection can potentially enhance the model's accuracy and revert back to the initial goal of predicting precise coordinates in the future.


### Data Collection
<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/7b1f8b622c4ca3e1bc93bc4ed3f2d1b66edb00cd/Assessment/Final%20Project/Report/src/trainingProcess.png" width="500" alt="Model training process">  <br>  <em>Figure 6. Model training process.</em>  </p>

An essential aspect of developing an effective AI-based indoor positioning system is collecting a robust and diverse dataset. In this project, five training sets were collected from the Connected Environment Lab located in UCL East, with each set containing approximately 3,000 depth images. The data collection process, as shown in Figure 6, involved gathering depth images, orientation, and acceleration data, along with the position of the user.

The quality and quantity of data significantly impact the performance of the AI model. Insufficient or inaccurate data can result in a poorly trained AI model that is unable to provide accurate predictions. Therefore, it is crucial to ensure that the dataset is comprehensive and representative of the different scenarios the AI model is likely to encounter.

To enhance the quality of depth images and reduce noise, we utilized the Oak-D camera's built-in depth filters. Specifically, we applied median and speckle filters to the captured depth images. The median filter helps eliminate noise by replacing each pixel's value with the median value of neighboring pixels, while the speckle filter removes isolated noise points or "speckles" from the images.

To calculate the user's location, Spectacular AI SDK (SpectacularAI, 2022) was employed, which leverages both the IMU information and depth images to estimate the user's relative coordinates. The SDK combines acceleration and orientation data from the IMU to determine the user's position and movement. Additionally, it corrects the calculated location by tracking features within the depth images, further enhancing the accuracy of the position estimation.

It is important to note that the Spectacular AI SDK provides the user's location in relative coordinates. To convert these relative coordinates to world coordinates, the initial location of the user must be known. By combining the starting position with the relative coordinates calculated by the SDK, the user's precise location can be determined in the indoor environment.




### Model Architecture Choices

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/AIarchitectures.png" width="500" alt="Trainined Model Architecture">  <br>  <em>Figure 7. Trainined Model Architecture.</em>  </p>

The TensorFlow model (Figure 7) is a Convolutional Neural Network (CNN) designed for processing depth map images to predict a user's indoor location within a grid. The purpose of using a CNN is to learn spatial features and patterns from the input images, making it an ideal choice for handling depth maps.

The first layer is **a convolutional layer** with 16 filters of size 3x3. This layer helps to capture local features from the input image. After this layer, **batch normalization** is applied to stabilize and accelerate training (De and Smith, 2020), followed by **a ReLU activation function** that introduces non-linearity and helps the network learn complex patterns (Chang and Chen, 2015). 

The second layer is a **max-pooling layer** with a pool size of 2x2, which reduces the spatial dimensions of the input, leading to a more compact representation and faster computation.

The model continues with **three more convolutional layers, each followed by a max-pooling layer**. These layers (with 32, 64, and 128 filters respectively) allow the model to learn higher-level features by capturing progressively larger spatial patterns in the depth map.

The **flattened output** is passed through a fully connected (dense) layer with 256 neurons and **a ReLU activation function**, which helps the network learn complex, high-level abstractions from the extracted features (Chang and Chen, 2015).

**A dropout layer** with a rate of 0.5 is added to prevent overfitting by randomly setting a fraction of the input units to zero during training (TensorFlow, 2023).

The final output layer is **a dense layer with 28 neurons and a softmax activation function,** which produces a probability distribution over the 28 grid cells representing the user's location. The softmax activation ensures that the sum of probabilities across all grid cells is equal to 1, making it suitable for multi-class classification tasks.

### Training Result

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/graph_trainingResult.png" width="500" alt="Model Loss and Model Accuracy Graph">  <br>  <em>Figure 8. Model Loss and Model Accuracy.</em>  </p>

The performance of the AI model was evaluated by comparing the predicted grid zones to the actual data points, which allowed us to assess the model's ability to accurately locate users within the building. The accuracy and loss values (Figure 8) obtained from the training process indicated that there was room for improvement in the model's performance. However, when we visualised the results on a 2D grid zone plane, as shown in Figure 9, the colors representing the predicted grid zones were found to be quite similar to the actual data point colors. This suggests that the model is able to provide reasonable estimations of user locations.

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/Visulisation_ResultMatrix.png" width="500" alt="Prediction of the trained model">  <br>  <em>Figure 9. Prediction of the trained model.</em>  </p>

I believe that the model can be further optimised. One possible approach to improve the model's performance is to collect more data that captures the unique features of each location within the building. This additional data would allow the AI model to learn the spatial characteristics of each zone more effectively, resulting in better predictions. Alternatively, refining the model architecture or exploring different optimization techniques could enhance the model's ability to learn from the available data and improve its overall performance.


## Application

### Application Architecture

<p align="center">  <img src="https://raw.githubusercontent.com/Lionel-Lim/casa0018/main/Assessment/Final%20Project/Report/src/ApplicationArchitectures.png" width="600" alt="Application architecture">  <br>  <em>Figure 10. Application architecture.</em>  </p>

The current application utilises an OpenVINO Intermediate Representation (IR) model converted from a TensorFlow model (.h5) for deployment on the Oak-D camera (Figure 10). Unfortunately, the converted OpenVINO IR model is not functioning as expected in the application due to an unknown issue.

It is common to encounter issues when converting models between different frameworks, as there can be discrepancies in layer implementations or optimisation techniques. Some common reasons for conversion problems include unsupported layers, differences in input preprocessing, and inconsistencies in weight initialization.

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

3. Optimise the AI model's architecture to reduce overfitting and improve generalization.

4. Utilise more powerful computing resources to enable faster training and experimentation.

5. Fix the trained model conversion issue.

  

### Weaknesses

The current AI model has some weaknesses, including its reliance on a smart camera and the limited amount of data collected. Additionally, the model's performance is affected by changes in the environment and the quality of the data collected.


## Bibliography

AKT II, 2022. UCL East Marshgate [WWW Document]. AKT II. URL https://www.akt-uk.com/projects/ucl-east-marshgate-i/ (accessed 4.22.23).
Chang, J.-R., Chen, Y.-S., 2015. Batch-normalized Maxout Network in Network. https://doi.org/10.48550/arXiv.1511.02583
De, S., Smith, S., 2020. Batch Normalization Biases Residual Blocks Towards the Identity Function in Deep Networks, in: Advances in Neural Information Processing Systems. Curran Associates, Inc., pp. 19964–19975.
DIY Indoor Autonomous Drone! - Part 2 (Kalibr & Calibration), 2018.
Luxonis, 2021. OAK-D [WWW Document]. Luxonis. URL https://shop.luxonis.com/products/oak-d (accessed 4.23.23).
Microsoft, 2022. Bing Image Creator.
OpenCV, Luxonis, 2021. OpenCV AI Kit: OAK—D [WWW Document]. OpenCV.AI. URL https://store.opencv.ai/products/oak-d (accessed 4.23.23).
Riccardo Giubilato, 2017. Visual inertial odometry on a budget!! [WWW Document]. RiccardoGiubilato. URL https://riccardogiubilato.github.io/visual/odometry/2017/12/12/Visual-Inertial-Odometry-On-A-Budget.html (accessed 2.2.23).
SpectacularAI, 2023. Spectacular AI SDK for OAK-D — spectacularAI documentation [WWW Document]. URL https://spectacularai.github.io/docs/sdk/python/latest/ (accessed 3.4.23).
SpectacularAI, 2022. Spectacular AI SDK.
TensorFlow, 2023. tf.keras.layers.Dropout | TensorFlow v2.12.0 [WWW Document]. TensorFlow. URL https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dropout (accessed 4.23.23).
Wei, Y., Akinci, B., 2019. A vision and learning-based indoor localization and semantic mapping framework for facility operations and management. Automation in Construction 107, 102915. https://doi.org/10.1016/j.autcon.2019.102915

----------

## Declaration of Authorship

I, Dongyoung Lim, confirm that the work presented in this assessment is my own. Where information has been derived from other sources, I confirm that this has been indicated in the work.

Dongyoung Lim

27 Apr 2023