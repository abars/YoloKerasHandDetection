# Yolo Keras Hand Detection

Implement Hand detection using Keras. (Under Constructing)

# Overview

## Functions

Hand Detection

## Requirements

Keras2 (Tensorflow backend)

Darknet

OpenCV

Python 2.7

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

## Train using Darknet

Here is a train.

`cd darknet`

`./darknet yolo train ../cfg/vivahand_tinyyolov1.cfg -train ../dataset/vivahand/detectiondata/train/pos/train.txt -backup ./backup/ -class 4`

## Test using Darknet

Here is a test.

`./darknet yolo test ../cfg/vivahand_tinyyolov1.cfg ./backup/vivahand_tinyyolov1_4000.weights ../dataset/vivahand/detectiondata/train/pos/1_0000003_0_0_0_6.png -class 4`

Here is a run.

`./darknet yolo demo ../cfg/vivahand_tinyyolov1.cfg ./backup/vivahand_tinyyolov1_4000.weights -class 4`



