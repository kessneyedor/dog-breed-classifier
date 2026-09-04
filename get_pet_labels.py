#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kessney Edor
# DATE CREATED: 09/04/2026                                  
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
    # Get list of filenames in the image folder
    filename_list = listdir(image_dir)

    # Create empty dictionary to hold results
    results_dic = dict()

    # Process each filename to create the pet label
    for filename in filename_list:
        # Skip hidden/system files (e.g. .DS_Store)
        if filename.startswith('.'):
            continue

        # Split filename on underscores, drop the extension first
        # e.g. "Boston_terrier_02259.jpg" -> split at '.' -> "Boston_terrier_02259"
        name_no_ext = filename.split('.')[0]

        # Split into individual word chunks by underscore
        word_list = name_no_ext.split('_')

        # Keep only alphabetic words (drops digits like "02259")
        pet_label_words = [word.lower() for word in word_list if word.isalpha()]

        # Join words back with a single space, and strip any stray whitespace
        pet_label = ' '.join(pet_label_words).strip()

        # Add to dictionary, warning if filename already exists (shouldn't happen)
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("Warning: Duplicate filename found -", filename)

    return results_dic