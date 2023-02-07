# @Autor : Mathis Gorvien
# @Date : 07-02-2023

# Create a folder for the data collection

# Import the libraries
import os
import datetime
import requests # request img from web
import shutil # save img locally

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

# Download the images from the web
def downloadImages(url):
    # Get the folder name
    folder = createFolder()
    # Download the images
    for i in range(1, 11):
        # Get the image name
        image_name = "image" + str(i) + ".jpg"
        # Get the image
        r = requests.get(url, stream=True)
        # Save the image
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(image_name, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        # Move the image to the folder
        os.rename(image_name, "./" + folder + "/" + image_name)

# Main function
def main():
    # Get the url
    url = input("Enter the url of the image : ")

    # Download the images
    downloadImages(url)

main()
# https://static.theprint.in/wp-content/uploads/2020/12/randomnumber.jpg?compress=true&quality=80&w=800&dpr=2.0

