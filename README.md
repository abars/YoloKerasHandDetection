# Yolo Keras Hand Detection

Implement Hand detection using Keras. (Under Constructing)

<img src="https://github.com/abars/YoloKerasHandDetection/blob/master/pretrain/predictions.jpg" width="50%" height="50%">
(image from viva hand dataset)

# Overview

## Functions

Hand Detection

## Requirements

Keras2 (Tensorflow backend)

OpenCV

Python 2.7 or 3.6

Darknet (for Training)

Perl (for Training)

# Test

## Download Pretrained-Model

`python download_model.py`

## Predict from Camera Image

Here is a run using pretrained model .

`python hand_demo.py`

# Train

## Create Dataset

Download viva hand dataset (detectiondata folder) and put in the datase/vivahand folder.

http://cvrr.ucsd.edu/vivachallenge/index.php/hands/hand-detection/

Create dataset/vivahand/detectiondata/train/pos annotations for darknet.

`perl annotation_vivahand_darknet.pl`

<img src="https://github.com/abars/YoloKerasHandDetection/blob/master/dataset/vivahand.png" width="50%" height="50%">

## Train using Darknet

Here is a training using YoloV2.

`cd darknet`

`./darknet detector train data/hand-one-class.data cfg/yolov2-tiny-train-one-class.cfg`

## Test using Darknet

Here is a test.

`./darknet detector demo data/hand-one-class.data cfg/yolov2-tiny-train-one-class.cfg backup-face/yolov2-tiny-train-one-class_28600.weights -c 0`

## Training Result

<img src="https://github.com/abars/YoloKerasHandDetection/blob/master/pretrain/yolov2-tiny-train-one-class_28600.jpg" width="50%" height="50%">

<http://www.abars.biz/keras/yolov2-tiny-one-class.cfg>

<http://www.abars.biz/keras/yolov2-tiny-train-one-class_28600.weights>

## Convert to Keras Model

Download YAD2K

https://github.com/allanzelener/YAD2K

This is a convert script.

`python3 yad2k.py yolov2-tiny-train-one-class.cfg yolov2-tiny-train-one-class_28600.weights yolov2_tiny-hand.h5`

This is a converted model.

<http://www.abars.biz/keras/yolov2_tiny-hand.h5>

