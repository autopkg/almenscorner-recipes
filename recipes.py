# -*- coding: utf-8 -*-

"""
This script creates a JSON file with a list of all AutoPkg recipes in the current repository.

Created by Tobias Almén
"""

import os
import plistlib
import urllib.parse
import json

# Directory containing AutoPkg recipe files
recipes_directory = os.getcwd()
main_repo = "almenscorner-recipes"

# List to store results
results = []

def process_recipe_file(file_path, file_name):
    """
    Process a single recipe file to extract name and url.

    :param file_path: The path to the recipe file
    :param file_name: The name of the recipe file
    """
    try:
        with open(file_path, "rb") as plist_file:
            plist_data = plistlib.load(plist_file)

        name = plist_data["Input"]["display_name"]
        
        if name == "%NAME%":
            name = plist_data["Input"]["NAME"]
        
        recipe_url = f"https://github.com/autopkg/{main_repo}/blob/main/" + os.path.basename(os.path.dirname(file_path)) + "/" + urllib.parse.quote_plus(file_name)

        results.append(
            {
                "name": name,
                "recipe_url": recipe_url,
            }
        )
        
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")


# Recursively traverse directories and find all .recipe files
for root, dirs, files in os.walk(recipes_directory):
    for file_name in files:
        if file_name.endswith(".intune.recipe"):
            file_path = os.path.join(root, file_name)
            process_recipe_file(file_path, file_name)
            
# write results to a json file
with open("recipes.json", "w") as f:
    json.dump(results, f, indent=4)