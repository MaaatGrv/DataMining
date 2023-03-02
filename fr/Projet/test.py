# Import Libraries
import os
import datetime
import requests
import shutil 
import random

# Create a folder for the data collection
def createFolder():
    # Get the current date and time
    now = datetime.datetime.now()
    # Create a folder with the current date and time
    folder = "images" + "-" + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
    # Create the folder
    os.chdir("./fr/Projet/images")
    os.mkdir(folder)
    # Return the flder name
    return folder

createFolder()

# load photos from the folder /fr/Projet/fleurs
def loadImages():
    # Create the folder & get the folder name
    folder = createFolder()

    # Load random images of flower from the foler /fr/Projet/fleurs
    # We will load 10 images and generate 10 random numbers between 1 and 4317 to get the images

    # Create a list of random numbers
    random_numbers = []
    # Generate 10 random numbers
    for i in range(10):
        # Generate a random number
        random_number = random.randint(1, 4317)
        # Add the random number to the list
        random_numbers.append(random_number)
    
    # Load the images using the folder name
    for i in range(1, 11):
        # Get the image name
        image_name = ".//fr/Projet/fleurs/fleur" + str(random_numbers[i-1]) + ".jpg"
        # Open the image
        image = open(image_name, "rb")
        # Save the image in the folder that we created
        with open("./" + folder + "/" + image_name, "wb") as f:
            f.write(image.read())
loadImages()