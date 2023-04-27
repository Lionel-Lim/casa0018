import depthai as dai

# Initialize pipeline
pipeline = dai.Pipeline()

# Configure Mono cameras
mono_left = pipeline.createMonoCamera()
mono_right = pipeline.createMonoCamera()
mono_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
mono_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

# Create StereoDepth node
stereo = pipeline.createStereoDepth()
stereo.setOutputDepth(True)
stereo.setOutputRectified(False)
stereo.setConfidenceThreshold(200)
mono_left.out.link(stereo.left)
mono_right.out.link(stereo.right)


# Closer-in minimum depth, disparity range is doubled (from 95 to 190):
extended_disparity = False
# Better accuracy for longer distance, fractional disparity 32-levels:
subpixel = False
# Better handling for occlusions:
lr_check = True

# Create a node that will produce the depth map (using disparity output as it's easier to visualize depth this way)
stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
# Options: MEDIAN_OFF, KERNEL_3x3, KERNEL_5x5, KERNEL_7x7 (default)
stereo.initialConfig.setMedianFilter(dai.MedianFilter.KERNEL_7x7)
stereo.setLeftRightCheck(lr_check)
stereo.setExtendedDisparity(extended_disparity)
stereo.setSubpixel(subpixel)

# Create neural network node
nn = pipeline.createNeuralNetwork()
nn.setBlobPath("../Model/model.xml")  # Set the path to the converted model
stereo.depth.link(nn.input)

# Create output node
xout_nn = pipeline.createXLinkOut()
xout_nn.setStreamName("nn")
nn.out.link(xout_nn.input)


# Run the pipeline
with dai.Device(pipeline) as device:
    q_nn = device.getOutputQueue(name="nn", maxSize=4, blocking=False)

    while True:
        in_nn = q_nn.get()  # Retrieve neural network output
        # Process the neural network output here
        output_data = in_nn.getFirstLayerFp16()
        predicted_number = output_data.index(max(output_data))
        print("Predicted number:", predicted_number)
