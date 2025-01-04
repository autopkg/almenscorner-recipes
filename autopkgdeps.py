# -*- coding: utf-8 -*-

"""
This script finds parent depedency repos and updates the README table with the results.

Created by Tobias Almén
"""

import os
import plistlib
import urllib.parse

from pytablewriter import MarkdownTableWriter

# Directory containing AutoPkg recipe files
recipes_directory = os.getcwd()
main_repo = "almenscorner-recipes"

# List to store results
results = []


def write_table(data):
    """
    This function creates the markdown table.

    :param data: The data to be written to the table
    :return: The Markdown table as a string
    """
    writer = MarkdownTableWriter(
        headers=["recipe", "dependency"],
        value_matrix=data,
    )
    return writer.dumps()


def process_recipe_file(file_path, file_name):
    """
    Process a single recipe file to extract dependencies.

    :param file_path: The path to the recipe file
    :param file_name: The name of the recipe file
    """
    try:
        with open(file_path, "rb") as plist_file:
            plist_data = plistlib.load(plist_file)

        parent_recipe_value = plist_data.get("ParentRecipe")
        if parent_recipe_value:
            recipe_url = f"https://github.com/autopkg/{main_repo}/blob/main/{urllib.parse.quote(file_path.split(f'{main_repo}/')[1])}"
            identifier = parent_recipe_value.split(".")[2]

            if identifier.endswith("-recipes"):
                formatted_dependency = identifier
            elif identifier == "autopkg" and parent_recipe_value.split(".")[3] in [
                "download",
                "pkg",
            ]:
                formatted_dependency = "recipes"
            else:
                identifier = parent_recipe_value.split(".")[2]
                formatted_dependency = (
                    f"{identifier}-recipes"
                    if not identifier.endswith("-recipes")
                    else identifier
                )

            dependency_url = f"https://github.com/autopkg/{formatted_dependency}"
            results.append(
                [
                    f"[{file_name}]({recipe_url})",
                    f"[{formatted_dependency}]({dependency_url})",
                ]
            )
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")


# Recursively traverse directories and find all .recipe files
for root, dirs, files in os.walk(recipes_directory):
    for file_name in files:
        if file_name.endswith(".recipe"):
            file_path = os.path.join(root, file_name)
            process_recipe_file(file_path, file_name)

if results:
    new_table = write_table(results)
    readme_path = os.path.join(recipes_directory, "README.md")

    with open(readme_path, "r") as readme_file:
        readme_contents = readme_file.read()

    # Correct start marker with exact match
    start_marker = "|"
    start_index = readme_contents.find(start_marker)

    if start_index != -1:
        # Locate the end of the table
        end_index = readme_contents.find(
            "\n\n", start_index
        )  # Find the double newline after the table
        if end_index == -1:  # If no double newline, assume end of file
            end_index = len(readme_contents)

        # Remove the leading pipe from new_table
        cleaned_table = new_table.lstrip("|").strip()

        # Update the README content
        updated_readme_contents = (
            readme_contents[
                : start_index + len(start_marker)
            ]  # Include the start_marker itself
            + cleaned_table
            + readme_contents[end_index:]
        )

        with open(readme_path, "w") as readme_file:
            readme_file.write(updated_readme_contents)

        print("README.md updated successfully.")
    else:
        print("Table start marker not found in README.md.")
else:
    print("No results to write to table.")
