# Facial Recognition with OpenCV

Project for AI subject. Using a small application of Artificial Vision. Python and OpenCV.

Daniel Hernández

# Usage

This app works in the terminal. Here are the instructions:

## Train

Execute the **project.py** file in the terminal. Select the first option. In order for this to work, there must be a mp4 video in the root folder **with the same name as typed in the terminal**.

![image](https://user-images.githubusercontent.com/36749947/142947198-ed2505e4-99f0-477f-893b-78ffa0e213d8.png)

The program will start playing the video and getting images of the face of the person. Once it finishes, you can add images for a new person, type **y**.

![image](https://user-images.githubusercontent.com/36749947/142947235-004e6f2e-5b3b-4312-8e2a-eb3906b89ae6.png)

If you type **n**, the script will begin to get the images and training the model. When this process finishes, an xml file will be created in the root, this is our model, **do not touch it**. The initial instructions will be displayed.
![image](https://user-images.githubusercontent.com/36749947/142947244-d784fd07-264f-4c4d-8837-1f39f686cffa.png)


## Test

Based on the model we built, we are now able to test the model to identify the faces it knows. Select the option 2 in the terminal. An indexed list will show the names of the people we know. Select one. A window will pop up, and with a frame and text, it will identify the face of the video. This videos **must be in the "samples" folder** with this structure:

> name-sample.mp4

The name beign the same as the one which we trained our model with.
Two parameters will show in the frame, a label and a trust value. The first one must be the same as the index of the option name previously displayed in the terminal. The second one indicates how accurate it is. When it is near 10,000, we could say it is a face that is not known.
