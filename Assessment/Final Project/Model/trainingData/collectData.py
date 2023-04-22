import depthai as dai
import spectacularAI
import json
import numpy as np
import cv2
import csv
from datetime import datetime

import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/dy/.local/lib/python3.10/site-packages/cv2/qt/plugins/platforms/'

timestamp = 0
currentTime = datetime.now().strftime('%m-%d %H:%M:%S')


def saveAsPng(outputFolder, frameId, cameraName, frame):
    # if not frame or not frame.image: return
    # fileName = outputFolder + "/" + cameraName + "_" + f'{frameId:05}' + ".png"
    fileName = '{}/{}_{}.png'.format(outputFolder, frameId, timestamp)
    # cv2.imwrite(fileName, cv2.cvtColor(frame.image.toArray(), cv2.COLOR_RGB2BGR))
    cv2.imwrite(fileName, frame)


def onMappingOutput(output):
    for frameId in output.updatedKeyFrames:
        keyFrame = output.map.keyFrames.get(frameId)
        if not keyFrame:
            continue
        else:
            frameSet = keyFrame.frameSet
            depth = frameSet.depthFrame
            if not depth or not depth.image:
                continue
            else:
                converted = cv2.cvtColor(depth.image.toArray(), cv2.COLOR_RGB2BGR)
                saveAsPng('/home/dy/aikit/test', frameId, 'depth', converted)

                # Display the processed depth map
                cv2.imshow("Processed Depth Map1", converted)
                cv2.setWindowTitle("Primary camera", "Primary camera #{}".format(frameId))
                cv2.waitKey(1)



def live_vio_reader():
    pipeline = dai.Pipeline()
    config = spectacularAI.depthai.Configuration()
    config.depthScaleCorrection = True
    vio_pipeline = spectacularAI.depthai.Pipeline(pipeline, config, onMappingOutput)

    with dai.Device(pipeline) as device,\
        vio_pipeline.startSession(device) as vio_session:
        # print(device.getOutputQueueNames())
        while True:
            out = vio_session.waitForOutput()
            # Display the processed depth map
            yield(json.loads(out.asJson()))

fields = ['timestamp', 'status', 'orientation', 'position', 'acceleration']

while True:
    print("Live")
    with open('/home/dy/aikit/data_{}.csv'.format(currentTime), mode='w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        writer.writerow(fields)

        vio_source = live_vio_reader()
        for vio_out in vio_source:
            timestamp = vio_out["time"]
            isTracking = vio_out["status"]
            acceleration = vio_out["acceleration"]
            orientation = vio_out["orientation"]
            position = vio_out["position"]
            values = [str(timestamp), isTracking, "/".join(str(value) for value in orientation.values()), "/".join(str(value) for value in position.values()), "/".join(str(value) for value in acceleration.values())]

            # Write the data to the CSV file
            writer.writerow(values)