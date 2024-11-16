#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then saves them to a file.
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    # Attempt to load the existing list from the file
    items = load_from_json_file("add_item.json")
except (FileNotFoundError, ValueError):
    # Initialize an empty list if the file doesn't exist or contains invalid JSON
    items = []

# Add command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, "add_item.json")

