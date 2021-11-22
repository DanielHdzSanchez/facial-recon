# Facial Recognition with OpenCV

Project for AI subject. Using a small application of Artificial Vision. Python and OpenCV.

Daniel Hernández

# Usage

This app works in the terminal. Here are the instructions:

## Train

Execute the **project.py** file in the terminal. Select the first option. In order for this to work, there must be a mp4 video in the root folder **with the same name as typed in the terminal**. The program will start playing the video and getting images of the face of the person. Once it finishes, you can add images for a new person, type **y**. If you type **n**, the script will begin to get the images and training the model. When this process finishes, an xml file will be created in the root, this is our model, **do not touch it**. The initial instructions will be displayed.

## Test

Based on the model we built, we are now able to test the model to identify the faces it knows. Select the option 2 in the terminal. An indexed list will show the names of the people we know. Select one. A window will pop up, and with a frame and text, it will identify the face of the video. This videos **must be in the "samples" folder** with this structure:

> name-sample.mp4

The name beign the same as the one which we trained our model with.
