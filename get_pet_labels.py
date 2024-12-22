
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: GBENOU Joris Martial Adechina
# DATE CREATED:  7/17/2024                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    pet_name=" "
    # Replace None with the results_dic dictionary that you created with this
    # function
    in_files = listdir(image_dir)
    results_dic={}
    for file_name in in_files:
      if file_name[0]!=".":
        # Extract the pet label from the filename
        pet_name = file_name.lower().rsplit('_', 1)[0].replace('_', ' ')
        #Eliminates number
        pet_name = ' '.join([word for word in pet_name.split() if word.isalpha()])
        #delete space
        pet_name = pet_name.strip()
        # If filename doesn't already exist in dictionary add it and its
        # pet label - otherwise print an error message because indicates 
        # duplicate files (filenames)
      if file_name not in results_dic:
        results_dic[file_name] = [pet_name]
      else:
        print("** Warning: Duplicate files exist in directory:", 
                     file_name)
      
    return results_dic

# Test the function
if __name__ == "__main__":
    # Replace 'path_to_your_images_folder' with the actual path to your images folder
    image_folder = '/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/pet_images'
    results = get_pet_labels(image_folder)
    print(results)