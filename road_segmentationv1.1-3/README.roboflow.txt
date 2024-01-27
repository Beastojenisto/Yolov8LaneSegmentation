
road_segmentationv1.1 - v3 2022-11-28 1:45pm
==============================

This dataset was exported via roboflow.com on January 20, 2023 at 6:32 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2766 images.
Road are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -10 and +10 degrees
* Random brigthness adjustment of between -44 and +44 percent
* Random exposure adjustment of between -25 and +25 percent
* Random Gaussian blur of between 0 and 1.75 pixels


