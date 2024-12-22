
# Dog Image Classification Project
This project uses pre-trained Convolutional Neural Networks (CNNs) to classify dog images for a citywide dog show registration system.

# Objectives
Identify if an image contains a dog or not.
Determine the breed of the dog in the image.
Compare the performance of different CNN architectures: AlexNet, VGG, and ResNet.
# Provided Files
classifier.py: A function to classify images using pre-trained CNNs.
test_classifier.py: An example script to demonstrate the classifier function.
# How to Run
Install required libraries:
bash
Copy code
pip install numpy torch torchvision pillow  
# Test the classifier with the provided script:
bash
Copy code
python test_classifier.py  
Use your scripts to classify images and evaluate performance.
# Notes
The project focuses on using Python skills, not building a classifier from scratch.
Certain breeds may look similar, leading to occasional misclassifications (e.g., Great Pyrenees vs. Kuvasz).
Future Improvements
Enhance the ability to differentiate between similar breeds.
